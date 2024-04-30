from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .leave_typeService import LeaveTypeService
from Schema.leave_typeSchema import LeaveTypeCreate
from Config.database import get_db

router = APIRouter(prefix="/leaveType", tags=["LeaveType"])

@router.get("/")
def get_all_leaveType(db: Session = Depends(get_db)):
    return LeaveTypeService.get_all_leaveType(db=db)

@router.post("/create_leaveType")
def create_leaveType(LeaveTypes: LeaveTypeCreate, db: Session = Depends(get_db)):
    return LeaveTypeService.create_leaveType(LeaveTypes, db)

