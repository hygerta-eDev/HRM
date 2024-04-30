from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TerminationReasonCreate(BaseModel):
    name: str
    slug: str
    created_at:datetime
    updated_at: datetime
    deleted_at:Optional[datetime]