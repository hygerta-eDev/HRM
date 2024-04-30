from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .holidayService import HolidayService
from Schema.holidaySchema import HolidayCreate
from Config.database import get_db

router = APIRouter(prefix="/holidays", tags=["Holidays"])

@router.get("/")
def get_all_holiday(db: Session = Depends(get_db)):
    return HolidayService.get_all_holiday(db=db)

@router.post("/create_holiday")
def create_holiday(Holidays: HolidayCreate, db: Session = Depends(get_db)):
    return HolidayService.create_holiday(Holidays, db)

