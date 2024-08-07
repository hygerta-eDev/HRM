from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class HolidayBase(BaseModel):
    date: datetime
    recurring: int
    user_id: int
    description: str

class HolidayCreate(HolidayBase):
    # created_at: datetime

    pass

class HolidayUpdate(HolidayBase):
    # updated_at: datetime]
    pass

    class Config:
        orm_mode = True
