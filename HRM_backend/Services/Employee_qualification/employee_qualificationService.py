from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeQualificationModel import Qualification
# from Models.ethnicitiesModel import Ethnicities

from Schema.employee_qualificationSchema import QualificationCreate


class QualificationService:
    @staticmethod
    def get_all_qualifications(db: Session = Depends(get_db)):
        return db.query(Qualification).all()
    
    def create_qualifications(Qualifications: QualificationCreate, db: Session = Depends(get_db)):

        db_qualification = Qualification(
            name=Qualifications.name,
            slug = Qualifications.slug,
            # manager_id=Department.manager_id
            # ethnicity_id=Department.ethnicity_id

        )

        db.add(db_qualification)
        db.commit()
        db.refresh(db_qualification)

        return db_qualification
