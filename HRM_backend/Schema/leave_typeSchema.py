from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeaveTypeBase(BaseModel):
    slug: str
    limit: int
    user_id:Optional[int]

class LeaveTypeCreate(LeaveTypeBase):
    # created_at: datetime
    pass

class LeaveTypeUpdate(LeaveTypeBase):
    # updated_at: datetime

    class Config:
        orm_mode = True

class LeaveTypeResponse(LeaveTypeBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
