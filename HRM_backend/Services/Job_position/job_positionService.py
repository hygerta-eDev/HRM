from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.jobPositionModel import JobPosition
from Schema.job_positionSchema import JobPositionCreate,JobPositionUpdate,JobPositionSchema
from Config.logging_utils import log_function_call
from sqlalchemy import func
from typing import Any, Optional


class JobPositionService:
    @staticmethod
    @log_function_call(entity_name="JobPosition")
    def get_all_jobPosition(db: Session = Depends(get_db)):
        return db.query(JobPosition).all()
    
    @staticmethod
    @log_function_call(entity_name="JobPosition")
    def get_all_active_jobPosition(db: Session = Depends(get_db)):
        return db.query(JobPosition).filter(JobPosition.deleted_at == None).all()
    
    @staticmethod
    @log_function_call(entity_name="JobPosition")
    def get_jobPosition_by_id(db: Session, entity_id: int)-> Optional[JobPositionSchema]:
        return db.query(JobPosition).filter(JobPosition.id == entity_id).first()
    
    @log_function_call(entity_name="JobPosition")
    def create_jobPosition(JobPositions: JobPositionCreate, db: Session = Depends(get_db))-> JobPositionCreate:

        db_jobPosition = JobPosition(
            name=JobPositions.name,
            slug=JobPositions.slug,
            department_id=JobPositions.department_id,
            user_id=JobPositions.user_id,
            active=JobPositions.active,

            # created_at=JobPositions.created_at
        )

        db.add(db_jobPosition)
        db_jobPosition.created_at = func.now()
        db.commit()
        db.refresh(db_jobPosition)
        # print(db_jobPosition)

        return db_jobPosition
    @staticmethod
    @log_function_call(entity_name="JobPosition")
    def update_jobPosition(jobPosition_id: int, jobPosition: JobPositionUpdate, db: Session = Depends(get_db)):

        db_jobPosition = db.query(JobPosition).filter(JobPosition.id == jobPosition_id).first()

        if db_jobPosition:
            changes = {}
            if db_jobPosition.name != jobPosition.name:
                changes['name'] = (db_jobPosition.name, jobPosition.name)
                db_jobPosition.name = jobPosition.name
            if db_jobPosition.slug != jobPosition.slug:
                changes['slug'] = (db_jobPosition.slug, jobPosition.slug)
                db_jobPosition.slug = jobPosition.slug
            if db_jobPosition.department_id != jobPosition.department_id:
                changes['department_id'] = (db_jobPosition.department_id, jobPosition.department_id)
                db_jobPosition.department_id = jobPosition.department_id
            if db_jobPosition.active != jobPosition.active:
                changes['active'] = (db_jobPosition.active, jobPosition.active)
                db_jobPosition.active = jobPosition.active

            if changes:
                db_jobPosition.updated_at = datetime.now()
                db.commit()
                db.refresh(db_jobPosition)

            return db_jobPosition
        else:
            raise HTTPException(status_code=404, detail="JobPosition not found")
    @staticmethod
    @log_function_call(entity_name="JobPosition")
    def delete_jobPosition(entity_id: int, db: Session = Depends(get_db)):
        db_jobPosition = db.query(JobPosition).filter(JobPosition.id == entity_id).first()

        if db_jobPosition:
            db_jobPosition.soft_delete()  
            db.commit()

        return db_jobPosition