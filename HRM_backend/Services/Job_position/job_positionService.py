from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.jobPositionModel import JobPosition
from Schema.job_positionSchema import JobPositionCreate,JobPositionUpdate


class JobPositionService:
    @staticmethod
    def get_all_jobPosition(db: Session = Depends(get_db)):
        return db.query(JobPosition).all()
    
    @staticmethod
    def get_jobPosition_by_id(db: Session, jobPosition_id: int):
        return db.query(JobPosition).filter(JobPosition.id == jobPosition_id).first()
    

    def create_jobPosition(JobPositions: JobPositionCreate, db: Session = Depends(get_db)):

        db_jobPosition = JobPosition(
            name=JobPositions.name,
            slug=JobPositions.slug,
            department_id=JobPositions.department_id,
            created_at=JobPositions.created_at
        )

        db.add(db_jobPosition)
        db.commit()
        db.refresh(db_jobPosition)
        # print(db_jobPosition)

        return db_jobPosition
    @staticmethod
    def update_jobPosition(jobPosition_id: int, jobPosition: JobPositionUpdate, db: Session = Depends(get_db)):

        db_jobPosition = db.query(JobPosition).filter(JobPosition.id == jobPosition_id).first()

        if db_jobPosition:
            if db_jobPosition.name is not None:
                db_jobPosition.name = jobPosition.name
            if db_jobPosition.slug is not None:
                db_jobPosition.slug = jobPosition.slug
            if db_jobPosition.department_id is not None:
                db_jobPosition.department_id = jobPosition.department_id
            # if db_jobPosition.updated_at is not None:
            #     db_jobPosition.updated_at = db_jobPosition.updated_at
            # if db_jobPosition.deleted_at is not None:
            #     db_jobPosition.deleted_at = jobPosition.deleted_at

            db_jobPosition.updated_at = datetime.now()

            db.commit()
            db.refresh(db_jobPosition)

        return db_jobPosition

    @staticmethod
    def delete_jobPosition(jobPosition_id: int, db: Session = Depends(get_db)):
        db_jobPosition = db.query(JobPosition).filter(JobPosition.id == jobPosition_id).first()

        if db_jobPosition:
            db.delete(db_jobPosition)
            db.commit()

        return db_jobPosition