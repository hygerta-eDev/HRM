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
    approved_by_id: Optional[int] = None
    approved_at: Optional[datetime] = None
    rejected_by_id: Optional[int] = None
    rejected_at: Optional[datetime] = None
    rejected_comment: Optional[str] = None
    status: Optional[str] = 'Inactive'
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

class LeaveCreate(LeaveBase):
    pass

class LeaveUpdate(LeaveBase):
    pass

class LeaveInDBBase(LeaveBase):
    id: int

    class Config:
        orm_mode = True

class Leave(LeaveInDBBase):
    pass
