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
    
    def create_ethnicity(Ethnicity: EthnicityCreate, db: Session = Depends(get_db)):

        db_ethnicity = Ethnicities(
            name=Ethnicity.name,
        )

        db.add(db_ethnicity)
        db.commit()
        db.refresh(db_ethnicity)

        return db_ethnicity
