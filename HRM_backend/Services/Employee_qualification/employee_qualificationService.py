from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeQualificationModel import Qualification
# from Models.ethnicitiesModel import Ethnicities
from Config.logging_utils import log_function_call
from typing import Any, Optional
from sqlalchemy import func
from Schema.employee_qualificationSchema import QualificationCreate,QualificationUpdate,QualificationSchema


class QualificationService:
    @staticmethod
    @log_function_call(entity_name="Qualification")
    def get_all_qualifications(db: Session = Depends(get_db)):
        return db.query(Qualification).all()
    
    @staticmethod
    @log_function_call(entity_name="Qualification")
    def get_all_active_qualifications(db: Session = Depends(get_db)):
        return db.query(Qualification).filter(Qualification.deleted_at == None).all()
    
    @staticmethod
    @log_function_call(entity_name="Qualification")
    def get_qualification_by_id(db: Session, entity_id: int):
        return db.query(Qualification).filter(Qualification.id == entity_id).first()
    
    @log_function_call(entity_name="Qualification")
    def create_qualifications(Qualifications: QualificationCreate, db: Session = Depends(get_db)) -> QualificationCreate:

        db_qualification = Qualification(
            name=Qualifications.name,
            slug = Qualifications.slug,
            user_id = Qualifications.user_id,
            # created_at=Qualifications.created_at
        )

        db.add(db_qualification)
        db_qualification.created_at=func.now()
        db.commit()
        db.refresh(db_qualification)

        return db_qualification
    
    @staticmethod
    @log_function_call(entity_name="Qualification")
    def update_qualifications(qualification_id: int, qualification: QualificationUpdate, entity_id: int, entity_type: Any, db: Session = Depends(get_db), user_id: int = 1, **kwargs):
        db_qualification = db.query(Qualification).filter(Qualification.deleted_at == None, Qualification.id == qualification_id).first()

        if not db_qualification:
            raise HTTPException(status_code=404, detail="Qualification not found")

        changes = {}
        for field, value in qualification.dict(exclude_unset=True).items():
            if getattr(db_qualification, field) != value:
                changes[field] = (getattr(db_qualification, field), value)
                setattr(db_qualification, field, value)

        kwargs['changes'] = changes  # Pass changes to kwargs for logging

        if changes:
            db_qualification.updated_at = func.now()
            db.commit()
            db.refresh(db_qualification)

        return db_qualification


    
    @staticmethod
    @log_function_call(entity_name="Qualification")
    def delete_qualification(entity_id: int, db: Session = Depends(get_db)):
        db_qualification = db.query(Qualification).filter(Qualification.id == entity_id).first()

        if db_qualification:
            db_qualification.soft_delete()
            db.commit()

        return db_qualification