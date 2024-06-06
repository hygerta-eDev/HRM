from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AssessmentQuestionCreate(BaseModel):
    title: str
    description: str
    options: str  # Assuming options are stored as a string, you can adjust if it's stored differently
    weight: float
    selected_option: Optional[str]  # Optional if not selected yet
    notes: Optional[str]
    assessment_id: int
    created_at:datetime
    user_id:int

class AssessmentQuestionUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    options: Optional[str]  # Assuming options are stored as a string, you can adjust if it's stored differently
    weight: float
    selected_option: Optional[str]  # Optional if not selected yet
    notes: Optional[str]
    assessment_id: Optional[int]
    updated_at: Optional[datetime]
    user_id:Optional[int]