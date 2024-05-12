from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .leave_typeService import LeaveTypeService
from Schema.leave_typeSchema import LeaveTypeCreate,LeaveTypeUpdate
from Config.database import get_db

router = APIRouter(prefix="/leaveType", tags=["LeaveType"])

@router.get("/")
def get_all_leaveType(db: Session = Depends(get_db)):
    return LeaveTypeService.get_all_leaveType(db=db)

@router.get("/{leaveType_id}")
def get_leaveType_by_id(leaveType_id: int, db: Session = Depends(get_db)):
    leaveType = LeaveTypeService.get_leaveType_by_id(db, leaveType_id)
    if leaveType is None:
        raise HTTPException(status_code=404, detail="LeaveType not found")
    return leaveType

@router.post("/create_leaveType")
def create_leaveType(LeaveTypes: LeaveTypeCreate, db: Session = Depends(get_db)):
    return LeaveTypeService.create_leaveType(LeaveTypes, db)

@router.put("/update_leaveType/{leaveType_id}")
def update_leaveType(leaveType_id: int, leaveType: LeaveTypeUpdate, db: Session = Depends(get_db)):
    return LeaveTypeService.update_leaveType(leaveType_id=leaveType_id, leaveType=leaveType, db=db)

@router.delete("/delete_department/{leaveType_id}")
def delete_department(leaveType_id: int, db: Session = Depends(get_db)):
    return LeaveTypeService.delete_department(leaveType_id=leaveType_id, db=db)