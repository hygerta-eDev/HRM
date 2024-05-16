from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InstitutionCreate(BaseModel):
    name: str
    slug: str
    created_at:datetime
    user_id:int
    # ethnicity_id:Optional[int]
class InstitutionUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    user_id:Optional[int]
    updated_at: Optional[datetime]
    # deleted_at:Optional[datetime]
    # ethnicity_id:Optional[int]
