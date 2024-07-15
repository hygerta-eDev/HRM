from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .leave_quotaService import LeaveQuoteService
from Schema.employee_leave_quotaSchema import EmployeeLeaveQuotaCreate, EmployeeLeaveQuotaUpdate,EmployeeLeaveQuotaCall
from Config.database import get_db
from Models.employeeLeaveQuotaModel import EmployeeLeaveQuota
from typing import List 
router = APIRouter(prefix="/leaveQuota", tags=["LeaveQuota"])

@router.get("/")
def get_all_leaveQuote(db: Session = Depends(get_db)):
    return LeaveQuoteService.get_all_leaveQuote(db=db)

@router.get("/active_leaveQuote")
def get_all_active_leaveQuote(db: Session = Depends(get_db)):
    return LeaveQuoteService.get_all_active_leaveQuote(db=db)

@router.get("/{leaveQuote_id}")
def get_leaveQuote(leaveQuote_id: int, db: Session = Depends(get_db)):
    leaveQuote = LeaveQuoteService.get_leaveQuote_by_id(db, leaveQuote_id)
    if leaveQuote is None:
        raise HTTPException(status_code=404, detail="leaveQuote not found")
    return leaveQuote

@router.post("/create_leaveQuota")
def create_leaveQuote(LeaveQuotas: EmployeeLeaveQuotaCreate, db: Session = Depends(get_db)):
    return LeaveQuoteService.create_leaveQuote(LeaveQuotas, db)


@router.put("/update_leaveQuotes/{leaveQuote_id}")
def update_leaveQuotes(leaveQuote_id: int, leaveQuote: EmployeeLeaveQuotaUpdate, db: Session = Depends(get_db)):
    leaveQuote=LeaveQuoteService.update_leaveQuotes(leaveQuote_id=leaveQuote_id, leaveQuote=leaveQuote, db=db)
    if leaveQuote is None:
        raise HTTPException(status_code=404, detail="leaveQuote not found or has been soft-deleted")
    return leaveQuote

@router.delete("/delete_leaveQuote/{leaveQuote_id}")
def delete_leaveQuote(leaveQuote_id: int, db: Session = Depends(get_db)):
    return LeaveQuoteService.delete_leaveQuote(leaveQuote_id=leaveQuote_id, db=db)


@router.get("/leaveType/leaveTypeInfo/{employee_id}/{leave_type_id}", response_model=EmployeeLeaveQuotaCall)
def get_leave_type_info(employee_id: int, leave_type_id: int, db: Session = Depends(get_db)):
    leave_quota = db.query(EmployeeLeaveQuota).filter(
        EmployeeLeaveQuota.employee_id == employee_id,
        EmployeeLeaveQuota.leave_type_id == leave_type_id,
        EmployeeLeaveQuota.deleted_at == None
    ).first()

    if not leave_quota:
        raise HTTPException(status_code=404, detail="Leave quota not found")

    return leave_quota

@router.get("/employee_leave_quotes/{employee_id}", response_model=List[EmployeeLeaveQuotaCall])
def get_employee_leave_quotes(employee_id: int, db: Session = Depends(get_db)):
    leave_quotes = LeaveQuoteService.get_leave_quotes_by_employee_id(db=db, employee_id=employee_id)
    if not leave_quotes:
        raise HTTPException(status_code=404, detail=f"No leave quotes found for employee_id: {employee_id}")
    return leave_quotes