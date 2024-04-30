from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .leaveService import LeaveService
from Schema.leaveSchema import LeaveCreate
from Config.database import get_db

router = APIRouter(prefix="/leaves", tags=["Leaves"])

@router.get("/")
def get_all_leaves(db: Session = Depends(get_db)):
    return LeaveService.get_all_leaves(db=db)

@router.post("/create_leaves")
def create_leaves(LeaveTypes: LeaveCreate, db: Session = Depends(get_db)):
    return LeaveService.create_leaves(LeaveTypes, db)

