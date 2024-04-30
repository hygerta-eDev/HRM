from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class TrainingBase(BaseModel):
    title: str
    start_date: date
    end_date: date
    description: str
    outcome: str
    user_id: int
    active: bool
    completed_at: Optional[datetime]
    created_at:datetime
    updated_at:datetime
    deleted_at:datetime

class TrainingCreate(TrainingBase):
    pass

class TrainingUpdate(TrainingBase):
    pass

class TrainingInDBBase(TrainingBase):
    id: int

    class Config:
        orm_mode = True

class Training(TrainingInDBBase):
    pass

class EmployeeTrainingCreate(BaseModel):
    employee_id: int
    training_id: int
