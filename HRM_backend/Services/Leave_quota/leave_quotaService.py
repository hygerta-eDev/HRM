from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeLeaveQuotaModel import EmployeeLeaveQuota
from Schema.employee_leave_quotaSchema import EmployeeLeaveQuotaSchema

class LeaveQuoteService:
    @staticmethod
    def get_all_leaveQuote(db: Session = Depends(get_db)):
        return db.query(EmployeeLeaveQuota).all()
    
    def create_leaveQuote(LeaveQuotes: EmployeeLeaveQuotaSchema, db: Session = Depends(get_db)):
 
        db_leaveQuote = EmployeeLeaveQuota(
            leave_type_id=LeaveQuotes.leave_type_id,
            employee_id=LeaveQuotes.employee_id,
            amount=LeaveQuotes.amount,
            taken=LeaveQuotes.taken,
            available=LeaveQuotes.available,
            carried_over=LeaveQuotes.carried_over,
            additional_approved=LeaveQuotes.additional_approved,
            created_at=LeaveQuotes.created_at,
            updated_at=LeaveQuotes.updated_at,
            deleted_at=LeaveQuotes.deleted_at,
            
        )

        db.add(db_leaveQuote)
        db.commit()
        db.refresh(db_leaveQuote)

        return db_leaveQuote

   