from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class TrainingBase(BaseModel):
    title: str
    start_date: date
    end_date: date
    description: str
    user_id: int
    active: bool
    completed_at: Optional[datetime]
    user_id:int


class TrainingCreate(TrainingBase):
    created_at:datetime


class TrainingUpdate(TrainingBase):
    outcome: str
    updated_at: Optional[datetime]
    

class TrainingInDBBase(TrainingBase):
    id: int

    class Config:
        orm_mode = True

class Training(TrainingInDBBase):
    pass

class EmployeeTrainingCreate(BaseModel):
    employee_id: int
    training_id: int
    created_at:datetime
    user_id:int

class EmployeeTrainingUpdate(BaseModel):
    employee_id: int
    training_id: int
    updated_at: Optional[datetime]
    user_id:int
    
class AssignEmployeeTraining(BaseModel):
    employee_id: int
    name: str
    last_name: str
    training_id: int
    created_at:datetime
    user_id:int