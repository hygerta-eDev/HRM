from fastapi import APIRouter, Depends, HTTPException, Form,Request
from sqlalchemy.orm import Session
from .leave_typeService import LeaveTypeService
from Models.leaveTypeModel import LeaveType
from Schema.leave_typeSchema import LeaveTypeCreate,LeaveTypeUpdate,LeaveTypeResponse
from Config.database import get_db
from typing import List


router = APIRouter(prefix="/leaveType", tags=["LeaveType"])

@router.get("/")
def get_all_leaveType(db: Session = Depends(get_db)):
    return LeaveTypeService.get_all_leaveType(db=db)

@router.get("/active_leaveTypes")
def get_all_active_leaveTypes(db: Session = Depends(get_db)):
    return LeaveTypeService.get_all_active_leaveTypes(db=db)

@router.get("/{leaveType_id}",response_model=LeaveTypeResponse)
def get_leaveType_by_id(leaveType_id: int, db: Session = Depends(get_db)):
    leaveType = LeaveTypeService.get_leaveType_by_id(db=db, entity_id=leaveType_id)
    if leaveType is None:
        raise HTTPException(status_code=404, detail="LeaveType not found")
    return leaveType

@router.post("/create_leaveType",response_model=LeaveTypeResponse)
def create_leaveType(LeaveTypes: LeaveTypeCreate, db: Session = Depends(get_db)):
    return LeaveTypeService.create_leaveType(LeaveTypes, db)

# @router.put("/update_leaveType/{leaveType_id}")
# def update_leaveType(leaveType_id: int, leaveType: LeaveTypeUpdate, db: Session = Depends(get_db)):
#     leaveType= LeaveTypeService.update_leaveType(leaveType_id=leaveType_id, leaveType=leaveType, db=db)
#     if leaveType is None:
#         raise HTTPException(status_code=404, detail="leaveType not found or has been soft-deleted")
#     return leaveType
@router.put("/update_leaveType/{leaveType_id}", response_model=LeaveTypeResponse)
def update_leaveType(leaveType_id: int, leaveType: LeaveTypeUpdate, request: Request, db: Session = Depends(get_db)):
    user_id = int(request.headers.get('X-User-Id', 1))
    entity_id = leaveType_id
    entity_type = LeaveType
    leaveType = LeaveTypeService.update_leaveType(leaveType_id=leaveType_id, leaveType=leaveType, db=db, user_id=user_id)
    if leaveType is None:
        raise HTTPException(status_code=404, detail="LeaveType not found or has been soft-deleted")
    return leaveType


@router.delete("/delete_department/{leaveType_id}")
def delete_department(leaveType_id: int, db: Session = Depends(get_db)):
    return LeaveTypeService.delete_department(entity_id=leaveType_id, db=db)

# @router.post("/seed-leave-types")
# def seed_leave_types_route():
#     db = get_db()
#     try:
#         seed_leave_types(db)
#         return {"message": "Leave types seeded successfully"}
#     except Exception as e:
#         return {"error": f"Failed to seed leave types: {str(e)}"}