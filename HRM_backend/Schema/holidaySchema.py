from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class HolidayBase(BaseModel):
    date: datetime
    recurring: int
    user_id: int
    description: str

class HolidayCreate(HolidayBase):
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    # pass

class Holiday(HolidayBase):
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
