from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DepartmentCreate(BaseModel):
    name: str
    slug: str
    institution_id:int
    created_at:datetime
    user_id:int
    # ethnicity_id:Optional[int]
class DepartmentUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    institution_id:Optional[int]
    user_id:Optional[int]
    updated_at: Optional[datetime]
    deleted_at:Optional[datetime]
    # ethnicity_id:Optional[int]
