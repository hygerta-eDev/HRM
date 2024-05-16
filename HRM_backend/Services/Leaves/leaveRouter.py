from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .leaveService import LeaveService
from Schema.leaveSchema import LeaveCreate,LeaveUpdate
from Config.database import get_db

router = APIRouter(prefix="/leaves", tags=["Leaves"])

@router.get("/")
def get_all_leaves(db: Session = Depends(get_db)):
    return LeaveService.get_all_leaves(db=db)
@router.get("/active_leaves")
def get_all_active_leaves(db: Session = Depends(get_db)):
    return LeaveService.get_all_active_leaves(db=db)

@router.get("/{leaves_id}")
def get_leaves_by_id(leaves_id: int, db: Session = Depends(get_db)):
    leaves = LeaveService.get_leaves_by_id(db, leaves_id)
    if leaves is None:
        raise HTTPException(status_code=404, detail="leaves not found")
    return leaves

@router.post("/create_leaves")
def create_leaves(LeaveTypes: LeaveCreate, db: Session = Depends(get_db)):
    return LeaveService.create_leaves(LeaveTypes, db)


@router.put("/update_leaves/{leave_id}")
def update_leaves(leave_id: int, leaves: LeaveUpdate, db: Session = Depends(get_db)):
    leaves=LeaveService.update_leaves(leave_id=leave_id, leaves=leaves, db=db)
    if leaves is None:
        raise HTTPException(status_code=404, detail="leaves not found or has been soft-deleted")
    return leaves

@router.delete("/delete_leaves/{leave_id}")
def delete_leaves(leave_id: int, db: Session = Depends(get_db)):
    return LeaveService.delete_leaves(leave_id=leave_id, db=db)
