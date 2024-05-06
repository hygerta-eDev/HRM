from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.ethnicitiesModel import Ethnicities
from Schema.ethnicitySchema import EthnicityCreate


class EthnicityService:
    @staticmethod
    def get_all_ethnicities(db: Session = Depends(get_db)):
        return db.query(Ethnicities).all()
    
    @staticmethod
    def get_ethnicities_by_id(db: Session, ethnicity_id: int):
        return db.query(Ethnicities).filter(Ethnicities.id == ethnicity_id).first()
    
    def create_ethnicity(Ethnicity: EthnicityCreate, db: Session = Depends(get_db)):

        db_ethnicity = Ethnicities(
            name=Ethnicity.name,
        )

        db.add(db_ethnicity)
        db.commit()
        db.refresh(db_ethnicity)

        return db_ethnicity
    
    @staticmethod
    def update_ethnicity(ethnicity_id: int, ethnicity: EthnicityCreate, db: Session = Depends(get_db)):
        db_ethnicities = db.query(Ethnicities).filter(Ethnicities.id == ethnicity_id).first()

        if db_ethnicities:
            if db_ethnicities.name is not None:
                db_ethnicities.name = ethnicity.name


            db.commit()
            db.refresh(db_ethnicities)

        return db_ethnicities
    @staticmethod
    def delete_ethnicity(ethnicity_id: int, db: Session = Depends(get_db)):
        db_ethnicities = db.query(Ethnicities).filter(Ethnicities.id == ethnicity_id).first()

        if db_ethnicities:
            db.delete(db_ethnicities)
            db.commit()

        return db_ethnicities