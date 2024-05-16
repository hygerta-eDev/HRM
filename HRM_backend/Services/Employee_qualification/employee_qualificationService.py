from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeQualificationModel import Qualification
# from Models.ethnicitiesModel import Ethnicities

from Schema.employee_qualificationSchema import QualificationCreate,QualificationUpdate


class QualificationService:
    @staticmethod
    def get_all_qualifications(db: Session = Depends(get_db)):
        return db.query(Qualification).all()
    @staticmethod
    def get_all_active_qualifications(db: Session = Depends(get_db)):
        return db.query(Qualification).filter(Qualification.deleted_at == None).all()
    @staticmethod
    def get_qualification_by_id(db: Session, qualification__id: int):
        return db.query(Qualification).filter(Qualification.id == qualification__id).first()
    
    def create_qualifications(Qualifications: QualificationCreate, db: Session = Depends(get_db)):

        db_qualification = Qualification(
            name=Qualifications.name,
            slug = Qualifications.slug,
            user_id = Qualifications.user_id,
            created_at=Qualifications.created_at
        )

        db.add(db_qualification)
        db.commit()
        db.refresh(db_qualification)

        return db_qualification
    
    @staticmethod
    def update_qualifications(qualification_id: int, qualification: QualificationUpdate, db: Session = Depends(get_db)):
        # db_qualification = db.query(Qualification).filter(Qualification.id == qualification_id).first()
        db_qualification = db.query(Qualification).filter(Qualification.deleted_at == None, Qualification.id == qualification_id).first()

        if db_qualification:
            if qualification.name is not None:
                db_qualification.name = qualification.name
            if db_qualification.slug is not None:
                db_qualification.slug = qualification.slug
            if qualification.user_id is not None:
                db_qualification.user_id = qualification.user_id
            if qualification.updated_at is not None:
                db_qualification.updated_at = qualification.updated_at

            db.commit()
            db.refresh(db_qualification)

        return db_qualification
    
    @staticmethod
    def delete_qualification(qualification_id: int, db: Session = Depends(get_db)):
        db_qualification = db.query(Qualification).filter(Qualification.id == qualification_id).first()

        if db_qualification:
            db_qualification.soft_delete()
            db.commit()

        return db_qualification