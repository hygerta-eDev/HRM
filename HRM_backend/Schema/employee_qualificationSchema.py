from pydantic import BaseModel
from typing import Optional

class QualificationCreate(BaseModel):
    name: str
    slug: str

class QualificationUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]