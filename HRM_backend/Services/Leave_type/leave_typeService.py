from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.leaveTypeModel import LeaveType
from Schema.leave_typeSchema import LeaveTypeCreate, LeaveTypeUpdate



class LeaveTypeService:
    @staticmethod
    def get_all_leaveType(db: Session = Depends(get_db)):
        return db.query(LeaveType).all()
    @staticmethod
    def get_all_active_leaveTypes(db: Session = Depends(get_db)):
        return db.query(LeaveType).filter(LeaveType.deleted_at == None).all()
  
    @staticmethod
    def get_leaveType_by_id(db: Session, leaveType_id: int):
        return db.query(LeaveType).filter(LeaveType.id == leaveType_id).first()
    def create_leaveType(LeaveTypes: LeaveTypeCreate, db: Session = Depends(get_db)):
 
        db_leaveType = LeaveType(
            slug=LeaveTypes.slug,
            limit=LeaveTypes.limit,
            user_id = LeaveTypes.user_id,
            created_at=LeaveTypes.created_at,
            
        )

        db.add(db_leaveType)
        db.commit()
        db.refresh(db_leaveType)

        return db_leaveType
    @staticmethod
    def update_leaveType(leaveType_id: int, leaveType: LeaveTypeUpdate, db: Session = Depends(get_db)):
        # db_leaveType = db.query(LeaveType).filter(LeaveType.id == leaveType_id).first()
        db_leaveType = db.query(LeaveType).filter(LeaveType.deleted_at == None, LeaveType.id == leaveType_id).first()

        if db_leaveType:
            if db_leaveType.limit is not None:
                db_leaveType.limit = leaveType.limit
            if db_leaveType.slug is not None:
                db_leaveType.slug = leaveType.slug
            if db_leaveType.updated_at is not None:
                db_leaveType.updated_at = leaveType.updated_at
            if db_leaveType.user_id is not None:
                db_leaveType.user_id = leaveType.user_id
            if db_leaveType.deleted_at is not None:
                db_leaveType.deleted_at = leaveType.deleted_at


            db.commit()
            db.refresh(db_leaveType)

        return db_leaveType
    @staticmethod
    def delete_department(leaveType_id: int, db: Session = Depends(get_db)):
        db_leaveType = db.query(LeaveType).filter(LeaveType.id == leaveType_id).first()

        if db_leaveType:
            db_leaveType.soft_delete() 
            db.commit()

        return db_leaveType
   