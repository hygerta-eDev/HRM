from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException,Request
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.leaveTypeModel import LeaveType
from Schema.leave_typeSchema import LeaveTypeCreate, LeaveTypeUpdate,LeaveTypeResponse
from Config.logging_utils import log_function_call
from sqlalchemy import func



class LeaveTypeService:
    @staticmethod
    @log_function_call(entity_name="LeaveTypes")
    def get_all_leaveType(db: Session = Depends(get_db)):
        return db.query(LeaveType).all()
    @staticmethod
    @log_function_call(entity_name="LeaveTypes")
    def get_all_active_leaveTypes(db: Session = Depends(get_db)):
        return db.query(LeaveType).filter(LeaveType.deleted_at == None).all()
  
    @staticmethod
    @log_function_call(entity_name="LeaveTypes")
    def get_leaveType_by_id(db: Session, entity_id: int):
        return db.query(LeaveType).filter(LeaveType.id == entity_id).first()
    
    @staticmethod
    @log_function_call(entity_name="LeaveTypes")
    def create_leaveType(LeaveTypes: LeaveTypeCreate, db: Session)-> LeaveTypeResponse:
 
        db_leaveType = LeaveType(
            slug=LeaveTypes.slug,
            limit=LeaveTypes.limit,
            user_id = LeaveTypes.user_id,
            # created_at=LeaveTypes.created_at,
            
        )

        db.add(db_leaveType)
        db_leaveType.created_at = func.now()
        db.commit()
        db.refresh(db_leaveType)

        return db_leaveType
    @staticmethod
    @log_function_call(entity_name="LeaveTypes")
    def update_leaveType(leaveType_id: int, leaveType: LeaveTypeUpdate, db: Session = Depends(get_db), **kwargs):
        db_leaveType = db.query(LeaveType).filter(LeaveType.deleted_at == None, LeaveType.id == leaveType_id).first()

        if not db_leaveType:
            raise HTTPException(status_code=404, detail="LeaveType not found")

        changes = {}
        for field, value in leaveType.dict(exclude_unset=True).items():
            if getattr(db_leaveType, field) != value:
                changes[field] = (getattr(db_leaveType, field), value)
                setattr(db_leaveType, field, value)

        kwargs['changes'] = changes  # Pass changes to kwargs for logging

        if changes:
            db_leaveType.updated_at = func.now()
            db.commit()
            db.refresh(db_leaveType)

        return db_leaveType

    
    
    @staticmethod
    @log_function_call(entity_name="LeaveTypes")
    def delete_department(entity_id: int, db: Session = Depends(get_db)):
        db_leaveType = db.query(LeaveType).filter(LeaveType.id == entity_id).first()

        if db_leaveType:
            db_leaveType.soft_delete() 
            db.commit()

        return db_leaveType
   