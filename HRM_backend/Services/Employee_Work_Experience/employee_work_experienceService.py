from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeWorkExperienceModel import WorkExperience

from Schema.work_experienceSchema import WorkExperienceCreate


class WorkExperienceService:
    @staticmethod
    def get_all_workExperience(db: Session = Depends(get_db)):
        return db.query(WorkExperience).all()
    
    def create_workExperience(WorkExperiences: WorkExperienceCreate, db: Session = Depends(get_db)):

        db_workexperience = WorkExperience(
            name=WorkExperiences.name,
            start = WorkExperiences.start,
            type = WorkExperiences.type,
            end = WorkExperiences.end,
            days = WorkExperiences.days,
            employee_id = WorkExperiences.employee_id

        )

        db.add(db_workexperience)
        db.commit()
        db.refresh(db_workexperience)

        return db_workexperience
