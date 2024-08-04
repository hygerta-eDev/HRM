

# from fastapi import FastAPI, APIRouter, Depends, HTTPException
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from ldap3 import Server, Connection, ALL
# from ldap3.core.exceptions import LDAPException
# from fastapi import FastAPI, Request, HTTPException, Form
# from fastapi.responses import HTMLResponse, RedirectResponse
# from uuid import uuid4
# from sqlalchemy import create_engine, Column, String
# from Config.database import Base,SessionLocal
# from ldap3 import Server, Connection, ALL
# from datetime import datetime, timedelta
# from sqlalchemy import Integer, DateTime
# from datetime import datetime, timedelta
# import os

# router = APIRouter(prefix="/ldap", tags=["ldaptest"])

# # HTTPBasic authentication scheme
# security = HTTPBasic()
# class Session(Base):
#     __tablename__ = 'session'
#     id = Column(String(36), primary_key=True)
#     username = Column(String, nullable=True)
#     session_timeout = Column(DateTime, nullable=True)
# # Dependency to check LDAP authentication
# def check_ldap_auth(credentials: HTTPBasicCredentials = Depends(security)):
#     LDAP_HOST = os.getenv('LDAP_HOST', '10.10.10.33')
#     LDAP_PORT = int(os.getenv('LDAP_PORT', 389))
#     LDAP_USE_SSL = os.getenv('LDAP_USE_SSL', False)
#     LDAP_BASE_DN = os.getenv('LDAP_BASE_DN', 'OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
#     LDAP_USER_RDN_ATTR = os.getenv('LDAP_USER_RDN_ATTR', 'CN')
#     LDAP_USER_LOGIN_ATTR = os.getenv('LDAP_USER_LOGIN_ATTR', 'sAMAccountName')
#     LDAP_BIND_USER_DN = os.getenv('LDAP_BIND_USER_DN', 'CN=HG-admin,OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
#     LDAP_BIND_USER_PASSWORD = os.getenv('LDAP_BIND_USER_PASSWORD', 'Password123')

#     if not LDAP_AUTH(LDAP_HOST, LDAP_PORT, LDAP_USE_SSL, LDAP_BASE_DN, LDAP_USER_RDN_ATTR, LDAP_USER_LOGIN_ATTR,
#                      LDAP_BIND_USER_DN, LDAP_BIND_USER_PASSWORD, credentials.username, credentials.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return credentials.username

# # LDAP authentication function
# def LDAP_AUTH(host, port, use_ssl, base_dn, user_rdn_attr, user_login_attr, bind_user_dn, bind_user_password, username, password):
#     try:
#         server = Server(f"ldap://{host}:{port}", use_ssl=use_ssl, get_info=ALL)
#         conn = Connection(server, user=f"{bind_user_dn}", password=bind_user_password, auto_bind=True)

#         conn.search(
#             search_base=base_dn,
#             search_filter=f"({user_login_attr}={username})",
#             search_scope="SUBTREE",
#             attributes=['memberOf']
#         )

#         if conn.response:
#             return True
#         else:
#             return False

#     except Exception as e:
#         print(f"LDAP Authentication Error: {str(e)}")
#         return False
#     finally:
#         try:
#             conn.unbind()
#         except Exception as e:
#             print(f"Error while unbinding LDAP connection: {str(e)}")

# # Example protected route using the dependency
# @router.get("/protected")
# async def protected_route(username: str = Depends(check_ldap_auth)):
#     return {"message": f"Hello, {username}! You have access to this protected route."}





# from fastapi import FastAPI, APIRouter, Depends, HTTPException
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from ldap3 import Server, Connection, ALL, SUBTREE
# from sqlalchemy import Column, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import Session
# from datetime import datetime, timedelta
# import os
# from Config.database import Base, get_db, SessionLocal, engine
# from uuid import uuid4

# # Define the Session table
# class Session(Base):
#     __tablename__ = 'session2'
#     id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
#     username = Column(String, nullable=True)
#     session_timeout = Column(DateTime, nullable=True)

# # Create the tables in the database
# Base.metadata.create_all(bind=engine)

# router = APIRouter(prefix="/ldap", tags=["ldaptest"])

# # HTTPBasic authentication scheme
# security = HTTPBasic()

# # Dependency to check LDAP authentication
# def check_ldap_auth(credentials: HTTPBasicCredentials = Depends(security)):
#     LDAP_HOST = os.getenv('LDAP_HOST', '10.10.10.33')
#     LDAP_PORT = int(os.getenv('LDAP_PORT', 389))
#     LDAP_USE_SSL = os.getenv('LDAP_USE_SSL', False)
#     LDAP_BASE_DN = os.getenv('LDAP_BASE_DN', 'OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
#     LDAP_USER_RDN_ATTR = os.getenv('LDAP_USER_RDN_ATTR', 'CN')
#     LDAP_USER_LOGIN_ATTR = os.getenv('LDAP_USER_LOGIN_ATTR', 'sAMAccountName')
#     LDAP_BIND_USER_DN = os.getenv('LDAP_BIND_USER_DN', 'CN=HG-admin,OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
#     LDAP_BIND_USER_PASSWORD = os.getenv('LDAP_BIND_USER_PASSWORD', 'Password123')

#     if not LDAP_AUTH(LDAP_HOST, LDAP_PORT, LDAP_USE_SSL, LDAP_BASE_DN, LDAP_USER_RDN_ATTR, LDAP_USER_LOGIN_ATTR,
#                      LDAP_BIND_USER_DN, LDAP_BIND_USER_PASSWORD, credentials.username, credentials.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return credentials.username

# # LDAP authentication function
# def LDAP_AUTH(host, port, use_ssl, base_dn, user_rdn_attr, user_login_attr, bind_user_dn, bind_user_password, username, password):
#     try:
#         server = Server(f"ldap://{host}:{port}", use_ssl=use_ssl, get_info=ALL)
#         conn = Connection(server, user=f"{bind_user_dn}", password=bind_user_password, auto_bind=True)

#         conn.search(
#             search_base=base_dn,
#             search_filter=f"({user_login_attr}={username})",
#             search_scope=SUBTREE,
#             attributes=['memberOf']
#         )

#         if conn.response:
#             return True
#         else:
#             return False

#     except Exception as e:
#         print(f"LDAP Authentication Error: {str(e)}")
#         return False
#     finally:
#         try:
#             conn.unbind()
#         except Exception as e:
#             print(f"Error while unbinding LDAP connection: {str(e)}")

# # Route to save users in the database upon successful LDAP authentication
# @router.get("/save_users")
# async def save_users_to_db(username: str = Depends(check_ldap_auth), db: Session = Depends(get_db)):
#     try:
#         db_user = db.query(Session).filter(Session.username == username).first()
#         if not db_user:
#             db_user = Session(username=username, session_timeout=datetime.now() + timedelta(hours=1))
#             db.add(db_user)
#             db.commit()
#             db.refresh(db_user)

#         return {"message": f"User {username} saved in the database"}

#     except Exception as e:
#         print(f"Error saving user to database: {str(e)}")
#         raise HTTPException(status_code=500, detail="Failed to save user in the database")

# # Example protected route using the dependency
# @router.get("/protected")
# async def protected_route(username: str = Depends(check_ldap_auth)):
#     return {"message": f"Hello, {username}! You have access to this protected route."}



# from fastapi import FastAPI, APIRouter, Depends, HTTPException
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from ldap3 import Server, Connection, ALL, SUBTREE
# from sqlalchemy import Column, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import Session
# from datetime import datetime, timedelta
# import os
# from Config.database import Base, get_db, SessionLocal, engine
# from uuid import uuid4

# # Define the Session table
# class Session(Base):
#     __tablename__ = 'session1'
#     id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
#     username = Column(String, nullable=True)
#     email = Column(String, nullable=True)  # Add email column
#     session_timeout = Column(DateTime, nullable=True)

# # Create the tables in the database
# Base.metadata.create_all(bind=engine)

# router = APIRouter(prefix="/ldap", tags=["ldaptest"])

# # HTTPBasic authentication scheme
# security = HTTPBasic()

# # Dependency to check LDAP authentication
# def check_ldap_auth(credentials: HTTPBasicCredentials = Depends(security)):
#     LDAP_HOST = os.getenv('LDAP_HOST', '10.10.10.33')
#     LDAP_PORT = int(os.getenv('LDAP_PORT', 389))
#     LDAP_USE_SSL = os.getenv('LDAP_USE_SSL', False)
#     LDAP_BASE_DN = os.getenv('LDAP_BASE_DN', 'OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
#     LDAP_USER_RDN_ATTR = os.getenv('LDAP_USER_RDN_ATTR', 'CN')
#     LDAP_USER_LOGIN_ATTR = os.getenv('LDAP_USER_LOGIN_ATTR', 'sAMAccountName')
#     LDAP_BIND_USER_DN = os.getenv('LDAP_BIND_USER_DN', 'CN=HG-admin,OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
#     LDAP_BIND_USER_PASSWORD = os.getenv('LDAP_BIND_USER_PASSWORD', 'Password123')

#     username = credentials.username

#     # Check if the provided credentials are an email address
#     if '@' in credentials.username:
#         LDAP_USER_LOGIN_ATTR = 'mail'  # Adjust attribute to search for email instead of sAMAccountName
#         username = credentials.username.split('@')[0]  # Use only the username part for LDAP search

#     if not LDAP_AUTH(LDAP_HOST, LDAP_PORT, LDAP_USE_SSL, LDAP_BASE_DN, LDAP_USER_RDN_ATTR, LDAP_USER_LOGIN_ATTR,
#                      LDAP_BIND_USER_DN, LDAP_BIND_USER_PASSWORD, username, credentials.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return username  # Return the username used for authentication

# # LDAP authentication function
# def LDAP_AUTH(host, port, use_ssl, base_dn, user_rdn_attr, user_login_attr, bind_user_dn, bind_user_password, username, password):
#     try:
#         server = Server(f"ldap://{host}:{port}", use_ssl=use_ssl, get_info=ALL)
#         conn = Connection(server, user=f"{bind_user_dn}", password=bind_user_password, auto_bind=True)

#         conn.search(
#             search_base=base_dn,
#             search_filter=f"({user_login_attr}={username})",
#             search_scope=SUBTREE,
#             attributes=['memberOf', 'mail']  # Include 'mail' attribute for email
#         )

#         if conn.response:
#             return conn.entries[0]['mail'].value if 'mail' in conn.entries[0] else None
#         else:
#             return None

#     except Exception as e:
#         print(f"LDAP Authentication Error: {str(e)}")
#         return None
#     finally:
#         try:
#             conn.unbind()
#         except Exception as e:
#             print(f"Error while unbinding LDAP connection: {str(e)}")

# # Route to save users in the database upon successful LDAP authentication
# @router.get("/save_users")
# async def save_users_to_db(username: str = Depends(check_ldap_auth), db: Session = Depends(get_db)):
#     try:
#         LDAP_HOST = os.getenv('LDAP_HOST', '10.10.10.33')
#         LDAP_PORT = int(os.getenv('LDAP_PORT', 389))
#         LDAP_USE_SSL = os.getenv('LDAP_USE_SSL', False)
#         LDAP_BASE_DN = os.getenv('LDAP_BASE_DN', 'OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
#         LDAP_USER_RDN_ATTR = os.getenv('LDAP_USER_RDN_ATTR', 'CN')
#         LDAP_USER_LOGIN_ATTR = os.getenv('LDAP_USER_LOGIN_ATTR', 'sAMAccountName')
#         LDAP_BIND_USER_DN = os.getenv('LDAP_BIND_USER_DN', 'CN=HG-admin,OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
#         LDAP_BIND_USER_PASSWORD = os.getenv('LDAP_BIND_USER_PASSWORD', 'Password123')

#         email = LDAP_AUTH(LDAP_HOST, LDAP_PORT, LDAP_USE_SSL, LDAP_BASE_DN, LDAP_USER_RDN_ATTR, LDAP_USER_LOGIN_ATTR,
#                           LDAP_BIND_USER_DN, LDAP_BIND_USER_PASSWORD, username, credentials.password)
        
#         db_user = db.query(Session).filter(Session.username == username).first()
        
#         if not db_user:
#             db_user = Session(username=username, email=email, session_timeout=datetime.now() + timedelta(hours=1))
#             db.add(db_user)
#             db.commit()
#             db.refresh(db_user)

#         return {"message": f"User {username} saved in the database"}

#     except Exception as e:
#         print(f"Error saving user to database: {str(e)}")
#         raise HTTPException(status_code=500, detail="Failed to save user in the database")

# # Example protected route using the dependency
# @router.get("/protected")
# async def protected_route(username: str = Depends(check_ldap_auth)):
#     return {"message": f"Hello, {username}! You have access to this protected route."}



from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from ldap3 import Server, Connection, ALL, SUBTREE
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import os

from Models.registersModel import Users
from Models.rolesModel import Roles
from Models.employeeRolesModels import EmployeeRoles
from Models.employeeModel import Employees  # Assuming this is your Employees model
from Config.database import Base, get_db, SessionLocal, engine

# Define the Session table
class Session(Base):
    __tablename__ = 'session5'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=True)
    session_timeout = Column(DateTime, nullable=True)

# Create the tables in the database
# Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/ldap", tags=["ldaptest"])

security = HTTPBasic()

def check_ldap_auth(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    LDAP_HOST = os.getenv('LDAP_HOST', '10.10.10.33')
    LDAP_PORT = int(os.getenv('LDAP_PORT', 389))
    LDAP_USE_SSL = os.getenv('LDAP_USE_SSL', False)
    LDAP_BASE_DN = os.getenv('LDAP_BASE_DN', 'OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
    LDAP_USER_RDN_ATTR = os.getenv('LDAP_USER_RDN_ATTR', 'CN')
    LDAP_USER_LOGIN_ATTR = os.getenv('LDAP_USER_LOGIN_ATTR', 'sAMAccountName')
    LDAP_BIND_USER_DN = os.getenv('LDAP_BIND_USER_DN', 'CN=HG-admin,OU=HG-users,OU=LDAP-users,DC=kgjk,DC=local')
    LDAP_BIND_USER_PASSWORD = os.getenv('LDAP_BIND_USER_PASSWORD', 'Password123')

    if not LDAP_AUTH(LDAP_HOST, LDAP_PORT, LDAP_USE_SSL, LDAP_BASE_DN, LDAP_USER_RDN_ATTR, LDAP_USER_LOGIN_ATTR,
                     LDAP_BIND_USER_DN, LDAP_BIND_USER_PASSWORD, credentials.username, credentials.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    username = credentials.username
    email = None  # Adjust to fetch email from LDAP if required

    # Check if the user exists in the local Users table
    db_user = db.query(Users).filter(Users.username == username).first()
    if not db_user:
        # Create a new user record if not exists
        db_user = Users(username=username, email=email)
        db.add(db_user)
    else:
        # Update user details if necessary
        db_user.email = email  # Update email if fetched from LDAP

    db.commit()
    db.refresh(db_user)

    return db_user.username 

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

        if conn.response:
            return True
        else:
            return False

    except Exception as e:
        print(f"LDAP Authentication Error: {str(e)}")
        return False
    finally:
        try:
            conn.unbind()
        except Exception as e:
            print(f"Error while unbinding LDAP connection: {str(e)}")

# router = APIRouter(prefix="/employeeRoles", tags=["EmployeeRoles"])

@router.get("/save_users")
async def save_users_to_db(username: str = Depends(check_ldap_auth), db: Session = Depends(get_db)):
    try:
        # Check if the user session exists; create one if it doesn't
        db_session = db.query(Session).filter(Session.username == username).first()
        if not db_session:
            db_session = Session(username=username, session_timeout=datetime.now() + timedelta(hours=1))
            db.add(db_session)
            db.commit()
            db.refresh(db_session)

        # Check if the user exists in the Users table; create one if it doesn't
        db_user = db.query(Users).filter(Users.username == username).first()
        if not db_user:
            db_user = Users(username=username, email=None)  # Update email fetching logic if needed
            db.add(db_user)
            db.commit()
            db.refresh(db_user)

        # Check if the employee exists in the Employees table; create one if it doesn't
        employee = db.query(Employees).filter(Employees.username == username).first()
        # if not employee:
        #     employee = Employees(username=username)  # Replace ... with appropriate fields
        #     db.add(employee)
        #     db.commit()
        #     db.refresh(employee)

        # Check if the role "employee" exists; handle if it doesn't exist
        role = db.query(Roles).filter(Roles.name == "Employee").first()
        # if not role:
        #     # Create the "employee" role if it doesn't exist
        #     role = Roles(name="employee")  # Adjust with appropriate role creation logic
        #     db.add(role)
        #     db.commit()
        #     db.refresh(role)

        # Check if the employee already has the "employee" role assigned
        existing_employee_role = db.query(EmployeeRoles).filter(
            EmployeeRoles.employee_id == employee.id,
            EmployeeRoles.role_id == role.id
        ).first()

        if not existing_employee_role:
            # Assign the "employee" role to the employee
            employee_role = EmployeeRoles(
                employee_id=employee.id,
                role_id=role.id,
                expires_at=None,  # Set as per your requirement
                user_id=db_user.user_id,  # Use user ID from Users table
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.add(employee_role)
            db.commit()
            db.refresh(employee_role)

        return {"message": f"User {username} logged in or created in the database and assigned 'employee' role",
                "employee_id": employee.id}

    except Exception as e:
        print(f"Error saving user to database: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to save user in the database")

# Example protected route using the dependency
@router.get("/protected")
async def protected_route(username: str = Depends(check_ldap_auth)):
    return {"message": f"Hello, {username}! You have access to this protected route."}

@router.get("/sessions")
async def get_all_sessions(db: Session = Depends(get_db)):
    sessions = db.query(Session).all()
    return sessions
