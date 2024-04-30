from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class JobPositionCreate(BaseModel):
    name: str
    slug: str
    department_id: int
    created_at:datetime
    updated_at: datetime
    deleted_at:Optional[datetime]