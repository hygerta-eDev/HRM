from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class JobPositionCreate(BaseModel):
    name: str
    slug: str
    department_id: int
    created_at:datetime


class JobPositionUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    department_id: Optional[int]
    updated_at: Optional[datetime]
    deleted_at:Optional[datetime]