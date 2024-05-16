from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.holidayModel import Holiday
from Schema.holidaySchema import HolidayCreate,HolidayUpdate

class HolidayService:
    @staticmethod
    def get_all_holiday(db: Session = Depends(get_db)):
        return db.query(Holiday).all()
    
    @staticmethod
    def get_all_active_holidays(db: Session = Depends(get_db)):
        return db.query(Holiday).filter(Holiday.deleted_at == None).all()
    
    @staticmethod
    def get_holiday_by_id(db: Session, holiday_id: int):
        return db.query(Holiday).filter(Holiday.id == holiday_id).first()
    
    def create_holiday(Holidays: HolidayCreate, db: Session = Depends(get_db)):
 
        db_holiday = Holiday(
            date=Holidays.date,
            recurring=Holidays.recurring,
            user_id=Holidays.user_id,
            description=Holidays.description,
            created_at=Holidays.created_at,

            
        )

        db.add(db_holiday)
        db.commit()
        db.refresh(db_holiday)

        return db_holiday
    @staticmethod
    def update_holiday(holiday_id: int, holiday: HolidayUpdate, db: Session = Depends(get_db)):
        db_holiday = db.query(Holiday).filter(Holiday.deleted_at == None, Holiday.id == holiday_id).first()

        if db_holiday:
            if holiday.date is not None:
                db_holiday.date = holiday.date
            if holiday.recurring is not None:
                db_holiday.recurring = holiday.recurring
            if db_holiday.description  is not None:
                db_holiday.description = holiday.description
            if holiday.user_id is not None:
                db_holiday.user_id = holiday.user_id
            if holiday.updated_at is not None:
                db_holiday.updated_at = holiday.updated_at
            db.commit()
            db.refresh(db_holiday)

        return db_holiday

    
    @staticmethod
    def delete_holiday(holiday_id: int, db: Session):
        db_holiday = db.query(Holiday).filter(Holiday.id == holiday_id).first()

        if db_holiday:
            db_holiday.soft_delete()  
            db.commit()

        return db_holiday
    
   