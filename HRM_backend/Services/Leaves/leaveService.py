from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.leavesModel import Leaves
from Schema.leaveSchema import LeaveCreate

class LeaveService:
    @staticmethod
    def get_all_leaves(db: Session = Depends(get_db)):
        return db.query(Leaves).all()
    
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
            updated_at=Leave.updated_at,
            deleted_at=Leave.deleted_at,     
        )

        db.add(db_leaves)
        db.commit()
        db.refresh(db_leaves)

        return db_leaves

   