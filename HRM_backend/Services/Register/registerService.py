from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.registersModel import Users
from Schema.registerSchema import UserCreate
import secrets
from passlib.hash import bcrypt
from fastapi.security import OAuth2PasswordBearer


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = secrets.token_hex(32)  
ALGORITHM = "HS256"

class UserService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    def authenticate_user(db: Session, username: str, password: str):
        user = db.query(Users).filter(Users.username == username).first()
        if not user:
            return False
        if not UserService.verify_password(password, user.password):
            return False
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

    
    @staticmethod
    def login_for_access_token(username: str, password: str, db: Session):
        user = UserService.authenticate_user(db, username, password)
        if not user:
            raise HTTPException(status_code=401, detail="Incorrect username or password")
        
        # Get the user ID
        user_id = user.user_id
        
        # Generate the access token
        access_token_expires = timedelta(minutes=30)
        access_token = UserService.create_access_token(
            data={"sub": user.username, "user_id": user_id}, expires_delta=access_token_expires
        )
        
        # Return both access token and user ID
        return {"access_token": access_token, "token_type": "bearer", "user_id": user_id}
