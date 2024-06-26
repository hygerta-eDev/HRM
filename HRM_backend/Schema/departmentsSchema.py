from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DepartmentCreate(BaseModel):
    name: str
    slug: str
    institution_id:int
    # created_at:datetime
    user_id:int
    active: bool
    # ethnicity_id:Optional[int]
class DepartmentUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    institution_id:Optional[int]
    active: Optional[bool]
    user_id:Optional[int]
    # updated_at: Optional[datetime]
    # ethnicity_id:Optional[int]
class Department(BaseModel):
    id: int
    name: str
    slug: str
    institution_id:int
    active: bool
    # created_at:datetime
    user_id:int