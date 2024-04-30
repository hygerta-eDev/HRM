from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AssessmentBase(BaseModel):
    employee_id: int
    # hr_employee_id: int
    user_id: int
    job_position_id: int
    evaluation_period: str
    rate: float = 0
    finished: bool = False
    status: str = 'created'
    performance_objectives: Optional[str] = None
    general_evaluation: Optional[str] = None
    employee_notes: Optional[str] = None
    employee_notes_date: Optional[str] = None

class AssessmentCreate(AssessmentBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    pass

class Assessment(AssessmentBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

    class Config:
        orm_mode = True
