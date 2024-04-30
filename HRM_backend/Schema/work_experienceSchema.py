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