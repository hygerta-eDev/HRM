from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeWorkExperienceModel import WorkExperience
from typing import List
from Schema.work_experienceSchema import WorkExperienceCreate,WorkExperienceUpdate,WorkExperienceCreates,WorkExperienceTest


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

    def create_work_experience(work_experiences: List[WorkExperienceCreate], db: Session):
        db_work_experiences = []
        
        for work_experience_data in work_experiences:
            db_work_experience = WorkExperience(
                name=work_experience_data.name,
                start=work_experience_data.start,
                type=work_experience_data.type,
                end=work_experience_data.end,
                employee_id=work_experience_data.employee_id,
                days=work_experience_data.days,
                user_id=work_experience_data.user_id,
                created_at=work_experience_data.created_at
            )
            db.add(db_work_experience)
            db_work_experiences.append(db_work_experience)
        
        db.commit()
        
        for db_work_experience in db_work_experiences:
            db.refresh(db_work_experience)
        
        return db_work_experiences
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
    def update_workExperiences_employee(employee_id: int, workExperience: WorkExperienceTest, db: Session = Depends(get_db)):
        # try:
            db_workExperience = db.query(WorkExperience).filter(
                WorkExperience.id == workExperience.id,
                WorkExperience.employee_id == employee_id,
                WorkExperience.deleted_at.is_(None)
            ).first()

            if db_workExperience:
                if workExperience.name is not None:
                    db_workExperience.name = workExperience.name
                if workExperience.start is not None:
                    db_workExperience.start = workExperience.start
                if workExperience.type is not None:
                    db_workExperience.type = workExperience.type
                if workExperience.end is not None:
                    db_workExperience.end = workExperience.end
                if workExperience.days is not None:
                    db_workExperience.days = workExperience.days
                if workExperience.employee_id is not None:
                    db_workExperience.employee_id = workExperience.employee_id
                if workExperience.user_id is not None:
                    db_workExperience.user_id = workExperience.user_id
                db_workExperience.updated_at = datetime.utcnow()  # Set updated_at to current time
                
                db.commit()
                db.refresh(db_workExperience)

                return db_workExperience  # Return the updated work experience
            else:
                return None

        # except Exception as e:
        #     print(f"Error updating work experience: {e}")
        #     raise HTTPException(status_code=500, detail="Error updating work experience")

    @staticmethod
    def delete_workExperience(workExperience_id: int, db: Session):
        db_workExperiences = db.query(WorkExperience).filter(WorkExperience.id == workExperience_id).first()

        if db_workExperiences:
            db_workExperiences.soft_delete()  
            db.commit()

        return db_workExperiences
