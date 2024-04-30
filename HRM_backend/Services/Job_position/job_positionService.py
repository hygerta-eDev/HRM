from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.jobPositionModel import JobPosition
from Schema.job_positionSchema import JobPositionCreate


class JobPositionService:
    @staticmethod
    def get_all_jobPosition(db: Session = Depends(get_db)):
        return db.query(JobPosition).all()
    
    def create_jobPosition(JobPositions: JobPositionCreate, db: Session = Depends(get_db)):

        db_jobPosition = JobPosition(
            name=JobPositions.name,
            slug=JobPositions.slug,
            department_id=JobPositions.department_id,
            created_at=JobPositions.created_at,
            updated_at=JobPositions.updated_at,
            deleted_at =JobPositions.deleted_at
        )

        db.add(db_jobPosition)
        db.commit()
        db.refresh(db_jobPosition)

        return db_jobPosition
