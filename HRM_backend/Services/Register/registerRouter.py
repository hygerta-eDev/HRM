from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .registerService import UserService
from Schema.registerSchema import UserCreate
from Config.database import get_db

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    return UserService.get_all_users(db=db)

@router.post("/create_user")
def create_user(User: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(User, db)

# @router.post("/login")
# def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
#     try:
#         # Authenticate user using LDAP and retrieve access token
#         return UserService.login_for_access_token(username, password, db)
    
#     except HTTPException as http_err:
#         raise http_err
    
#     except Exception as err:
#         print(f"Error logging in: {str(err)}")
#         raise HTTPException(status_code=500, detail="Failed to log in")
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    try:
        # Authenticate user using LDAP and retrieve access token
        return UserService.login_for_access_token(login_request.username, login_request.password, db)
    
    except HTTPException as http_err:
        raise http_err
    
    except Exception as err:
        print(f"Error logging in: {str(err)}")
        raise HTTPException(status_code=500, detail="Failed to log in")