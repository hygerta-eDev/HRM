from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeWorkExperienceModel import WorkExperience

from Schema.work_experienceSchema import WorkExperienceCreate,WorkExperienceUpdate


class WorkExperienceService:
    @staticmethod
    def get_all_workExperience(db: Session = Depends(get_db)):
        return db.query(WorkExperience).all()
    @staticmethod
    def get_all_active_workExperiences(db: Session = Depends(get_db)):
        return db.query(WorkExperience).filter(WorkExperience.deleted_at == None).all()
    @staticmethod
    def get_workExperience_by_id(db: Session, workExperience_id: int):
        return db.query(WorkExperience).filter(WorkExperience.id == workExperience_id).first()
    
    def create_workExperience(WorkExperiences: WorkExperienceCreate, db: Session = Depends(get_db)):

        db_workexperience = WorkExperience(
            name=WorkExperiences.name,
            start = WorkExperiences.start,
            type = WorkExperiences.type,
            end = WorkExperiences.end,
            employee_id = WorkExperiences.employee_id,
            days = WorkExperiences.days,
            user_id = WorkExperiences.user_id,
            created_at = WorkExperiences.created_at


        )

        db.add(db_workexperience)
        db.commit()
        db.refresh(db_workexperience)

        return db_workexperience
    @staticmethod
    def update_workExperiences(workExperience_id: int, workExperience: WorkExperienceUpdate, db: Session = Depends(get_db)):
        db_workExperiences = db.query(WorkExperience).filter(WorkExperience.deleted_at == None, WorkExperience.id == workExperience_id).first()

        if db_workExperiences:
            if workExperience.name is not None:
                db_workExperiences.name = workExperience.name
            if workExperience.start is not None:
                db_workExperiences.start = workExperience.start
            if workExperience.type is not None:
                db_workExperiences.type = workExperience.type
            if workExperience.end is not None:
                db_workExperiences.end = workExperience.end
            if workExperience.days is not None:
                db_workExperiences.days = workExperience.days
            if workExperience.employee_id is not None:
                db_workExperiences.employee_id = workExperience.employee_id
            if workExperience.user_id is not None:
                db_workExperiences.user_id = workExperience.user_id
            if workExperience.updated_at is not None:
                db_workExperiences.updated_at = workExperience.updated_at
            db.commit()
            db.refresh(db_workExperiences)

        return db_workExperiences

    
    @staticmethod
    def delete_workExperience(workExperience_id: int, db: Session):
        db_workExperiences = db.query(WorkExperience).filter(WorkExperience.id == workExperience_id).first()

        if db_workExperiences:
            db_workExperiences.soft_delete()  
            db.commit()

        return db_workExperiences
