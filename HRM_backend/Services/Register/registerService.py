from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException,status,Header
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.registersModel import Users
from Models.employeeModel import Employees
from typing import Any, Callable, Optional

from Models.employeeRolesModels import EmployeeRoles
from Config.ldap_router import check_ldap_auth
from Schema.registerSchema import UserCreate
import secrets
from passlib.hash import bcrypt
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta
from ldap3 import Server, Connection, ALL, SUBTREE
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = secrets.token_hex(32)  
ALGORITHM = "HS256"
ROLE_PERMISSIONS = {
    1: ['view_dashboard', 'edit_profile'],  # Role 1 permissions
    2: ['view_reports'],                    # Role 2 permissions
    3: ['manage_users', 'view_dashboard'],  # Role 3 permissions
    # Add other roles and permissions as needed
}
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Role Permissions
ROLE_PERMISSIONS = {
    1: ['view_dashboard', 'edit_profile'],  # Role 1 permissions
    2: ['view_reports'],                    # Role 2 permissions
    3: ['manage_users', 'view_dashboard'],  # Role 3 permissions
    # Add other roles and permissions as needed
}

# JWT Decoding
@staticmethod
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        return payload
    except JWTError:
        raise credentials_exception
credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


# Get Current User

class UserService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    def get_current_user(token: str = Depends(oauth2_scheme)) -> Any:
        user = decode_token(token)
        return user
    @staticmethod
    def get_user_id_from_header(x_user_id: str = Header(None)) -> int:
        if x_user_id is None:
            raise HTTPException(status_code=400, detail="User ID header missing")
        try:
            return int(x_user_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid User ID header format")
    @staticmethod
    def get_all_users(db: Session = Depends(get_db)):
        return db.query(Users).all()
    
    def create_user(User: UserCreate, db: Session = Depends(get_db)):
        hashed_password = bcrypt.hash(User.password)
        hashed_confirmation = bcrypt.hash(User.password_confirmation)# Hash the password

        db_userCreate = Users(
            name=User.name,
            username=User.username,
            email=User.email,
            email_verified_at=User.email_verified_at,
            password=hashed_password,
            password_confirmation=hashed_confirmation,
            active=User.active,
            banned_until=User.banned_until,
            language=User.language
        )

        db.add(db_userCreate)
        db.commit()
        db.refresh(db_userCreate)

        return db_userCreate

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def authenticate_user(db: Session, username: str):
        user = db.query(Users).filter(Users.username == username).first()
        if not user:
            return False
        # if not UserService.verify_password(password, user.password):
        #     return False
        return user

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    # @staticmethod
    # def login_for_access_token(username: str, password: str, db: Session = Depends(get_db)):
    #     user = UserService.authenticate_user(db, username, password)
    #     if not user:
    #         raise HTTPException(status_code=401, detail="Incorrect username or password")
    #     access_token_expires = timedelta(minutes=30)
    #     access_token = UserService.create_access_token(
    #         data={"sub": user.username}, expires_delta=access_token_expires
    #     )
    #     return {"access_token": access_token, "token_type": "bearer"}

    # def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    #     print("Received token:", token)

    #     try:
    #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #         username: str = payload.get("sub")
    #         user = db.query(Users).filter(Users.username == username).first()
    #         if user is None:
    #             raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    #         return user
    #     except JWTError:
    #         raise HTTPException(status_code=401, detail="Invalid token")
    
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def get_user_roles(user_id: int, db: Session):
        user_roles = (
            db.query(EmployeeRoles.role_id)
            .filter(EmployeeRoles.user_id == user_id)
            .all()
        )
        if not user_roles:
            return []
        return [role.role_id for role in user_roles]
    
    def get_user_permissions(user_roles):
        permissions = set()
        for role in user_roles:
            permissions.update(ROLE_PERMISSIONS.get(role, []))
        return permissions

    @staticmethod
    def assign_default_role(user_id: int, employee_id: int, db: Session):
        default_role_id = 3  # Assuming 3 is the role ID for Employee
        new_role = EmployeeRoles(user_id=user_id, employee_id=employee_id, role_id=default_role_id)
        db.add(new_role)
        db.commit()

    @staticmethod
    def login_for_access_token(username: str, password: str, db: Session):
        try:
            # LDAP Configuration
            LDAP_HOST = os.getenv('LDAP_HOST', '10.10.10.33')
            LDAP_PORT = int(os.getenv('LDAP_PORT', 389))
            LDAP_USE_SSL = os.getenv('LDAP_USE_SSL', False)
            LDAP_BASE_DN = os.getenv('LDAP_BASE_DN', 'OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
            LDAP_USER_RDN_ATTR = os.getenv('LDAP_USER_RDN_ATTR', 'CN')
            LDAP_USER_LOGIN_ATTR = os.getenv('LDAP_USER_LOGIN_ATTR', 'sAMAccountName')
            LDAP_BIND_USER_DN = os.getenv('LDAP_BIND_USER_DN', 'CN=HG-admin,OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
            LDAP_BIND_USER_PASSWORD = os.getenv('LDAP_BIND_USER_PASSWORD', 'Password123')

            # Authenticate user via LDAP
            if not UserService.LDAP_AUTH(LDAP_HOST, LDAP_PORT, LDAP_USE_SSL, LDAP_BASE_DN, LDAP_USER_RDN_ATTR, 
                                         LDAP_USER_LOGIN_ATTR, LDAP_BIND_USER_DN, LDAP_BIND_USER_PASSWORD, 
                                         username, password):
                raise HTTPException(status_code=401, detail="Invalid username or password")

            # Fetch user details
            user_details = db.query(Users).filter(Users.username == username).first()

            # Check if user exists in the employee table
            employee_details = db.query(Employees).filter(Employees.username == username).first()

            if user_details:
                # Update user details if they exist
                user_details.email_verified_at = datetime.utcnow()
            else:
                # Create new user record
                new_user = Users(username=username, email_verified_at=datetime.utcnow())
                db.add(new_user)
                db.commit()
                db.refresh(new_user)  # Get the new user ID
                user_details = new_user

            # If employee details exist, assign role and log in
            if employee_details:
                user_id = user_details.user_id
                name = f"{employee_details.name} {employee_details.last_name}" if employee_details.name and employee_details.last_name else employee_details.name
                employee_id = employee_details.id

                # Assign the default role to the new user if no role is assigned yet
                if not UserService.get_user_roles(user_id, db):
                    UserService.assign_default_role(user_id, employee_id, db)

                roles = UserService.get_user_roles(user_id, db)
                permissions = UserService.get_user_permissions(roles)

                # Generate the access token
                access_token_expires = timedelta(minutes=30)
                access_token = UserService.create_access_token(
                    data={"sub": username, "user_id": user_id, "employee_id": employee_id, "roles": roles, "permissions": list(permissions)}, expires_delta=access_token_expires
                )

                # Return access token, user ID, roles, permissions, and name
                return {"access_token": access_token, "token_type": "bearer", "user_id": user_id, "employee_id": employee_id, "roles": roles, "permissions": list(permissions), "name": name}
            else:
                raise HTTPException(status_code=404, detail="Employee not found")

        except HTTPException as http_err:
            raise http_err

        except Exception as err:
            print(f"Error logging in: {str(err)}")
            raise HTTPException(status_code=500, detail="Failed to log in")

    @staticmethod
    def LDAP_AUTH(host, port, use_ssl, base_dn, user_rdn_attr, user_login_attr, bind_user_dn, bind_user_password, username, password):
        try:
            server = Server(f"ldap://{host}:{port}", use_ssl=use_ssl, get_info=ALL)
            conn = Connection(server, user=f"{bind_user_dn}", password=bind_user_password, auto_bind=True)

            conn.search(
                search_base=base_dn,
                search_filter=f"({user_login_attr}={username})",
                search_scope=SUBTREE,
                attributes=['memberOf']
            )

            if not conn.response:
                return False

            # Attempt to bind as the user
            user_dn = conn.response[0]['dn']
            user_conn = Connection(server, user=user_dn, password=password, auto_bind=True)
            return user_conn.bind()

        except Exception as e:
            print(f"LDAP Authentication Error: {str(e)}")
            return False

        finally:
            try:
                conn.unbind()
            except Exception as e:
                print(f"Error while unbinding LDAP connection: {str(e)}")

    # @staticmethod
    # def login_for_access_token(username: str = Depends(check_ldap_auth), password: str, db: Session):
    #     user = UserService.authenticate_user(db, username)
    #     if not user:
    #         raise HTTPException(status_code=401, detail="Incorrect username or password")
        
    #     # Fetch user details including user_id and name
    #     user_details = db.query(Users).filter(Users.username == username).first()
    #     user_id = user_details.user_id
    #     name = user_details.name
        
    #     # Get the user's role
    #     role = UserService.get_user_role(user_id, db)
        
    #     # Generate the access token
    #     access_token_expires = timedelta(minutes=30)
    #     access_token = UserService.create_access_token(
    #         data={"sub": user.username, "user_id": user_id, "role": role}, expires_delta=access_token_expires
    #     )
        
    #     # Return access token, user ID, role, and name
    #     return {"access_token": access_token, "token_type": "bearer", "user_id": user_id, "role": role, "name": name}

    # @staticmethod
    # def login_for_access_token(username: str, password: str, db: Session):
    #     user = UserService.authenticate_user(db, username, password)
    #     if not user:
    #         raise HTTPException(status_code=401, detail="Incorrect username or password")
        
    #     # Get the user ID and role
    #     user_id = user.user_id
    #     role = UserService.get_user_role(user_id, db)
        
    #     # Generate the access token
    #     access_token_expires = timedelta(minutes=30)
    #     access_token = UserService.create_access_token(
    #         data={"sub": user.username, "user_id": user_id, "role": role}, expires_delta=access_token_expires
    #     )
        
    #     # Return both access token, user ID, and role
    #     return {"access_token": access_token, "token_type": "bearer", "user_id": user_id, "role": role}
