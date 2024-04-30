from pydantic import BaseModel
from typing import Optional

class AssessmentQuestionCreate(BaseModel):
    title: str
    description: str
    options: str  # Assuming options are stored as a string, you can adjust if it's stored differently
    weight: float
    selected_option: Optional[str]  # Optional if not selected yet
    notes: Optional[str]
    assessment_id: int
