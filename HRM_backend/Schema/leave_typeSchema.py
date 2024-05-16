from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeaveTypeBase(BaseModel):
    slug: str
    limit: int
    user_id:int

class LeaveTypeCreate(LeaveTypeBase):
    created_at: datetime

class LeaveTypeUpdate(LeaveTypeBase):
    updated_at: datetime

    class Config:
        orm_mode = True
