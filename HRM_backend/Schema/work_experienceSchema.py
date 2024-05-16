from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkExperienceCreate(BaseModel):
    name: str
    start: datetime
    type: str
    end:datetime
    days: int
    employee_id:int
    created_at:datetime
    user_id:int

class WorkExperienceUpdate(BaseModel):
    name: Optional[str]
    start: Optional[datetime]
    type: Optional[str]
    end:Optional[datetime]
    days: Optional[int]
    user_id:Optional[int]
    employee_id:Optional[int]
    updated_at: Optional[datetime]