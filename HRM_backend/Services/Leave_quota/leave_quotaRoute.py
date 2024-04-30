from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .leave_quotaService import LeaveQuoteService
from Schema.employee_leave_quotaSchema import EmployeeLeaveQuotaSchema
from Config.database import get_db

router = APIRouter(prefix="/leaveQuota", tags=["LeaveQuota"])

@router.get("/")
def get_all_leaveQuote(db: Session = Depends(get_db)):
    return LeaveQuoteService.get_all_leaveQuote(db=db)

@router.post("/create_leaveQuota")
def create_leaveQuote(LeaveQuotas: EmployeeLeaveQuotaSchema, db: Session = Depends(get_db)):
    return LeaveQuoteService.create_leaveQuote(LeaveQuotas, db)

