from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeLeaveQuotaModel import EmployeeLeaveQuota
from Schema.employee_leave_quotaSchema import EmployeeLeaveQuotaCreate, EmployeeLeaveQuotaUpdate
from typing import List

class LeaveQuoteService:
    @staticmethod
    def get_all_leaveQuote(db: Session = Depends(get_db)):
        return db.query(EmployeeLeaveQuota).all()
    
    @staticmethod
    def get_all_active_leaveQuote(db: Session = Depends(get_db)):
        return db.query(EmployeeLeaveQuota).filter(EmployeeLeaveQuota.deleted_at == None).all()
    
    @staticmethod
    def get_leaveQuote_by_id(db: Session, leaveQuote_id: int):
        return db.query(EmployeeLeaveQuota).filter(EmployeeLeaveQuota.employee_id == leaveQuote_id).first()
    
    def create_leaveQuote(LeaveQuotes: EmployeeLeaveQuotaCreate, db: Session = Depends(get_db)):
 
        db_leaveQuote = EmployeeLeaveQuota(
            leave_type_id=LeaveQuotes.leave_type_id,
            employee_id=LeaveQuotes.employee_id,
            amount=LeaveQuotes.amount,
            taken=LeaveQuotes.taken,
            available=LeaveQuotes.available,
            carried_over=LeaveQuotes.carried_over,
            additional_approved=LeaveQuotes.additional_approved,
            created_at=LeaveQuotes.created_at,
            user_id=LeaveQuotes.user_id            
        )

        db.add(db_leaveQuote)
        db.commit()
        db.refresh(db_leaveQuote)

        return db_leaveQuote

    @staticmethod
    def update_leaveQuotes(leaveQuote_id: int, leaveQuote: EmployeeLeaveQuotaUpdate, db: Session = Depends(get_db)):
        db_leaveQuote = db.query(EmployeeLeaveQuota).filter(EmployeeLeaveQuota.deleted_at == None, EmployeeLeaveQuota.employee_id == leaveQuote_id).first()

        if db_leaveQuote:
            if leaveQuote.leave_type_id is not None:
                db_leaveQuote.leave_type_id = leaveQuote.leave_type_id
            if leaveQuote.employee_id is not None:
                db_leaveQuote.employee_id = leaveQuote.employee_id
            if leaveQuote.leave_period_id is not None:
                db_leaveQuote.leave_period_id = leaveQuote.leave_period_id
            if leaveQuote.amount is not None:
                db_leaveQuote.amount = leaveQuote.amount
            if leaveQuote.taken is not None:
                db_leaveQuote.taken = leaveQuote.taken
            if leaveQuote.available is not None:
                db_leaveQuote.available = leaveQuote.available
            if leaveQuote.carried_over is not None:
                db_leaveQuote.carried_over = leaveQuote.carried_over
            if leaveQuote.additional_approved is not None:
                db_leaveQuote.additional_approved = leaveQuote.additional_approved
            if leaveQuote.user_id is not None:
                db_leaveQuote.user_id = leaveQuote.user_id
            if leaveQuote.updated_at is not None:
                db_leaveQuote.updated_at = leaveQuote.updated_at
            db.commit()
            db.refresh(db_leaveQuote)

        return db_leaveQuote

    
    @staticmethod
    def delete_leaveQuote(leaveQuote_id: int, db: Session):
        db_leaveQuote = db.query(EmployeeLeaveQuota).filter(EmployeeLeaveQuota.employee_id == leaveQuote_id).first()

        if db_leaveQuote:
            db_leaveQuote.soft_delete()  
            db.commit()

        return db_leaveQuote
    @staticmethod
    def get_leave_quotes_by_employee_id(db: Session, employee_id: int) -> List[EmployeeLeaveQuota]:
        return db.query(EmployeeLeaveQuota).filter(
            EmployeeLeaveQuota.employee_id == employee_id,
            EmployeeLeaveQuota.deleted_at.is_(None)  # Assuming soft delete with deleted_at field
        ).all()