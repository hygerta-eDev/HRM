from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.holidayModel import Holiday
from Schema.holidaySchema import HolidayCreate

class HolidayService:
    @staticmethod
    def get_all_holiday(db: Session = Depends(get_db)):
        return db.query(Holiday).all()
    
    def create_holiday(Holidays: HolidayCreate, db: Session = Depends(get_db)):
 
        db_holiday = Holiday(
            date=Holidays.date,
            recurring=Holidays.recurring,
            user_id=Holidays.user_id,
            description=Holidays.description,
            created_at=Holidays.created_at,
            updated_at=Holidays.updated_at,
            deleted_at=Holidays.deleted_at,
            
        )

        db.add(db_holiday)
        db.commit()
        db.refresh(db_holiday)

        return db_holiday

   