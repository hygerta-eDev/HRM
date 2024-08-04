from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .enums.work_experience import Work_experience

class WorkExperienceCreate(BaseModel):
    name: str
    start: datetime
    type: Optional[Work_experience]
    end:datetime
    days: int
    employee_id:int
    created_at:datetime
    user_id:int
    # updated_at: Optional[datetime]


class WorkExperienceUpdate(BaseModel):
    name: Optional[str]
    start: Optional[datetime]
    type: Optional[Work_experience]
    end:Optional[datetime]
    days: Optional[int]
    user_id:Optional[int]
    employee_id:Optional[int]
    updated_at: Optional[datetime]

class WorkExperienceCreates(BaseModel):
    name: str
    start: datetime
    type: str
    end: datetime
    employee_id: int
    days: int
    user_id: int
    created_at: datetime

class WorkExperienceTest(BaseModel):
    id: int
    name: Optional[str]
    start: Optional[datetime]
    type: Optional[Work_experience] 
    end: Optional[datetime]
    days: Optional[int]
    employee_id: Optional[int]
    created_at: Optional[datetime]
    user_id: Optional[int]
    updated_at: Optional[datetime]  

    class Config:
        orm_mode = True