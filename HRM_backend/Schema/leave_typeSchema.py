from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeaveTypeBase(BaseModel):
    slug: str
    limit: int

class LeaveTypeCreate(LeaveTypeBase):
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    # pass

class LeaveType(LeaveTypeBase):
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
