from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.leaveTypeModel import LeaveType
from Schema.leave_typeSchema import LeaveTypeCreate

class LeaveTypeService:
    @staticmethod
    def get_all_leaveType(db: Session = Depends(get_db)):
        return db.query(LeaveType).all()
    
    def create_leaveType(LeaveTypes: LeaveTypeCreate, db: Session = Depends(get_db)):
 
        db_leaveType = LeaveType(
            slug=LeaveTypes.slug,
            limit=LeaveTypes.limit,
            created_at=LeaveTypes.created_at,
            updated_at=LeaveTypes.updated_at,
            deleted_at=LeaveTypes.deleted_at,
            
        )

        db.add(db_leaveType)
        db.commit()
        db.refresh(db_leaveType)

        return db_leaveType

   