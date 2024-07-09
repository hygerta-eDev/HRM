from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LeaveBase(BaseModel):
    start_date: datetime
    end_date: datetime
    days: Optional[int] = 0
    leave_type_id: int
    user_id: int
    employee_id: int
    # approved_by_id: Optional[int] = None
    # approved_at: Optional[datetime] = None
    # rejected_by_id: Optional[int] = None
    # rejected_at: Optional[datetime] = None
    # rejected_comment: Optional[str] = None
    status: Optional[str] = 'Inactive'

class LeaveCreate(LeaveBase):
    created_at: Optional[datetime]

class LeaveUpdate(LeaveBase):
    approved_by_id: Optional[int] = None
    approved_at: Optional[datetime] = None
    rejected_by_id: Optional[int] = None
    rejected_at: Optional[datetime] = None
    rejected_comment: Optional[str] = None
    updated_at: Optional[datetime]

class LeaveInDBBase(LeaveBase):
    id: int

    class Config:
        orm_mode = True

class Leave(LeaveInDBBase):
    pass
class LeaveStatusUpdate(BaseModel):
    status: str

