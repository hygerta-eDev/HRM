from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .leaveService import LeaveService
from Schema.leaveSchema import LeaveCreate,LeaveUpdate,LeaveStatusUpdate,LeaveInDBBase
from Config.database import get_db
from typing import List
from Models.leavesModel import Leaves
from Models.employeeModel import Employees
from fastapi.responses import JSONResponse

from Models.employeeLeaveQuotaModel import EmployeeLeaveQuota
from datetime import datetime

router = APIRouter(prefix="/leaves", tags=["Leaves"])

@router.get("/")
def get_all_leaves(db: Session = Depends(get_db)):
    return LeaveService.get_all_leaves(db=db)
@router.get("/active_leaves")
def get_all_active_leaves(db: Session = Depends(get_db)):
    return LeaveService.get_all_active_leaves(db=db)
@router.get("/active_leaves/aproved")
def get_all_active_leaves_aproved(db: Session = Depends(get_db)):
    return LeaveService.get_all_active_leaves_aproved(db=db)

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
def update_leaves(leave_id: int, leave_update: LeaveUpdate, db: Session = Depends(get_db)):
    updated_leave = LeaveService.update_leaves(leave_id=leave_id, leave_update=leave_update, db=db)
    if updated_leave is None:
        raise HTTPException(status_code=404, detail="Leave not found or has been soft-deleted")
    return updated_leave


@router.delete("/delete_leaves/{leave_id}")
def delete_leaves(leave_id: int, db: Session = Depends(get_db)):
    return LeaveService.delete_leaves(leave_id=leave_id, db=db)


@router.get("/leave/pending", response_model=List[LeaveInDBBase])
def get_pending_leaves(db: Session = Depends(get_db)):
    pending_leaves = db.query(Leaves).filter(Leaves.status == "Pending").all()
    if not pending_leaves:
        raise HTTPException(status_code=404, detail="No pending leave requests found.")
    return pending_leaves

@router.get("/leave/status_leave/{status_leave}", response_model=List[LeaveInDBBase])
def get_pending_leaves(status_leave: str, db: Session = Depends(get_db)):
    leave_records = db.query(Leaves).filter(Leaves.status == status_leave).all()
    if not leave_records:
        raise HTTPException(status_code=404, detail="No leave requests found for the given status.")
    return leave_records

@router.get("/leaves/user/{user_id}", response_model=List[LeaveInDBBase])
def read_user_leaves(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Employees).filter(Employees.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.leaves

@router.patch("/leave/{leave_id}/status")
def update_leave_status(leave_id: int, leave_status: LeaveUpdate, db: Session = Depends(get_db)):
    leave = db.query(Leaves).filter(Leaves.id == leave_id).first()
    if not leave:
        raise HTTPException(status_code=404, detail="Leave request not found.")
    
    leave.status = leave_status.status
    leave.updated_at = datetime.utcnow()  # Assuming you have an updated_at field

    if leave_status.status == "Approved":
        leave.approved_by_id = leave_status.approved_by_id
        leave.approved_at = leave_status.approved_at

        leave_quota = db.query(EmployeeLeaveQuota).filter(
            EmployeeLeaveQuota.employee_id == leave.employee_id,
            EmployeeLeaveQuota.leave_type_id == leave.leave_type_id,
            EmployeeLeaveQuota.deleted_at == None
        ).first()

        if not leave_quota:
            raise HTTPException(status_code=404, detail="Leave quota not found for the specified employee and leave type.")
        
        if leave_quota.available < leave.days:
            raise HTTPException(status_code=400, detail="Insufficient leave days available.")
        
        leave_quota.available -= leave.days
        leave_quota.taken += leave.days

        db.add(leave_quota)
    elif leave_status.status == "Rejected":
        leave.rejected_by_id = leave_status.rejected_by_id
        leave.rejected_at = leave_status.rejected_at
        leave.rejected_comment = leave_status.rejected_comment

    db.add(leave)
    db.commit()
    db.refresh(leave)
    
    return {"detail": f"Leave request has been {leave_status.status.lower()}ed successfully."}

# @router.get("/total_leaves/{employee_id}")
# async def total_leaves(employee_id: int, db: Session = Depends(get_db)):
#     try:
#         total_leaves = LeaveService.sum_leaves_for_employee(employee_id, db)
#         return JSONResponse(content={"total_leaves": total_leaves})
#     except HTTPException as e:
#         return JSONResponse(status_code=e.status_code, content={"error": e.detail})
@router.get("/count_leaves/{employee_id}", response_model=int)
def count_leaves(employee_id: int, db: Session = Depends(get_db)):
    try:
        total_leaves = LeaveService.count_leaves_for_employee(employee_id, db)
        return total_leaves
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))