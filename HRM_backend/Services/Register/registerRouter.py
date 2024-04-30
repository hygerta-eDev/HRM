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

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    return UserService.login_for_access_token(username, password, db)