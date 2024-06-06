from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class JobPositionSchema(BaseModel):
    id: int
    name: str
    slug: str
    department_id: int
    user_id: int
    active: bool
    created_at:datetime
    updated_at: Optional[datetime]
    deleted_at:Optional[datetime]
class JobPositionCreate(BaseModel):
    name: str
    slug: str
    department_id: int
    user_id: int
    active: bool
    # created_at:datetime


class JobPositionUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    department_id: Optional[int]
    user_id:Optional[int]
    active: Optional[bool]
    updated_at: Optional[datetime]
    # deleted_at:Optional[datetime]