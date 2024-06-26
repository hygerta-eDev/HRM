from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .leave_quotaService import LeaveQuoteService
from Schema.employee_leave_quotaSchema import EmployeeLeaveQuotaCreate, EmployeeLeaveQuotaUpdate
from Config.database import get_db

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
