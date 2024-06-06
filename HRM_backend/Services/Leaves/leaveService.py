from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.leavesModel import Leaves
from Schema.leaveSchema import LeaveCreate,LeaveUpdate

class LeaveService:
    @staticmethod
    def get_all_leaves(db: Session = Depends(get_db)):
        return db.query(Leaves).all()
    
    @staticmethod
    def get_all_active_leaves(db: Session = Depends(get_db)):
        return db.query(Leaves).filter(Leaves.deleted_at == None).all()
    
    @staticmethod
    def get_leaves_by_id(db: Session, leaves_id: int):
        return db.query(Leaves).filter(Leaves.id == leaves_id).first()
    
    def create_leaves(Leave: LeaveCreate, db: Session = Depends(get_db)):
 
        db_leaves = Leaves(
            start_date=Leave.start_date,
            end_date=Leave.end_date,
            days=Leave.days,
            leave_type_id=Leave.leave_type_id,
            user_id=Leave.user_id,
            employee_id=Leave.employee_id,
            approved_by_id=Leave.approved_by_id,
            approved_at=Leave.approved_at,
            rejected_by_id=Leave.rejected_by_id,
            rejected_at=Leave.rejected_at,
            rejected_comment=Leave.rejected_comment,
            status=Leave.status,            
            created_at=Leave.created_at,
        )

        db.add(db_leaves)
        db.commit()
        db.refresh(db_leaves)

        return db_leaves

    @staticmethod
    def update_leaves(leave_id: int, leaves: LeaveUpdate, db: Session = Depends(get_db)):
        db_leaves = db.query(Leaves).filter(Leaves.deleted_at == None, Leaves.id == leave_id).first()

        if db_leaves:
            if leaves.start_date is not None:
                db_leaves.start_date = leaves.start_date
            if leaves.end_date is not None:
                db_leaves.end_date = leaves.end_date
            if leaves.days is not None:
                db_leaves.days = leaves.days
            if leaves.leave_type_id is not None:
                db_leaves.leave_type_id = leaves.leave_type_id
            if leaves.employee_id is not None:
                db_leaves.employee_id = leaves.employee_id
            if leaves.approved_by_id is not None:
                db_leaves.approved_by_id = leaves.approved_by_id
            if leaves.approved_at is not None:
                db_leaves.approved_at = leaves.approved_at
            if leaves.rejected_by_id is not None:
                db_leaves.rejected_by_id = leaves.rejected_by_id
            if leaves.rejected_at is not None:
                db_leaves.rejected_at = leaves.rejected_at
            if leaves.rejected_comment is not None:
                db_leaves.rejected_comment = leaves.rejected_comment
            if leaves.status is not None:
                db_leaves.status = leaves.status
            if leaves.user_id is not None:
                db_leaves.user_id = leaves.user_id
            if leaves.updated_at is not None:
                db_leaves.updated_at = leaves.updated_at
            db.commit()
            db.refresh(db_leaves)

        return db_leaves

    
    @staticmethod
    def delete_leaves(leave_id: int, db: Session):
        db_leaves = db.query(Leaves).filter(Leaves.id == leave_id).first()

        if db_leaves:
            db_leaves.soft_delete()  
            db.commit()

        return db_leaves