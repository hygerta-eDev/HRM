from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .holidayService import HolidayService
from Schema.holidaySchema import HolidayCreate,HolidayUpdate
from Config.database import get_db

router = APIRouter(prefix="/holidays", tags=["Holidays"])

@router.get("/")
def get_all_holiday(db: Session = Depends(get_db)):
    return HolidayService.get_all_holiday(db=db)

@router.get("/active_holidays")
def get_all_active_holidays(db: Session = Depends(get_db)):
    return HolidayService.get_all_active_holidays(db=db)

@router.get("/{holiday_id}")
def get_holiday_by_id(holiday_id: int, db: Session = Depends(get_db)):
    holiday = HolidayService.get_holiday_by_id(db, holiday_id)
    if holiday is None:
        raise HTTPException(status_code=404, detail="holiday not found")
    return holiday



@router.post("/create_holiday")
def create_holiday(Holidays: HolidayCreate, db: Session = Depends(get_db)):
    return HolidayService.create_holiday(Holidays, db)


@router.put("/update_holiday/{holiday_id}")
def update_holiday(holiday_id: int, holiday: HolidayUpdate, db: Session = Depends(get_db)):
    holiday=HolidayService.update_holiday(holiday_id=holiday_id, holiday=holiday, db=db)
    if holiday is None:
        raise HTTPException(status_code=404, detail="holiday not found or has been soft-deleted")
    return holiday

@router.delete("/delete_holiday/{holiday_id}")
def delete_holiday(holiday_id: int, db: Session = Depends(get_db)):
    return HolidayService.delete_holiday(holiday_id=holiday_id, db=db)
