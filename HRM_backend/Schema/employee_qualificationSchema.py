from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class QualificationCreate(BaseModel):
    name: str
    slug: str
    user_id:int
    
class QualificationUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    user_id:Optional[int]
    # updated_at: Optional[datetime]


class QualificationSchema(BaseModel):
    id:int
    name: str
    slug: str
    created_at:datetime
    user_id:int
    