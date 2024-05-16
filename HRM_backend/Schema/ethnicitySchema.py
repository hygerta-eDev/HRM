from pydantic import BaseModel, constr, validator
from datetime import datetime
from Config.database import get_db
from typing import Optional

class EthnicityCreate(BaseModel):
    created_at:datetime
    user_id:int
    name: str

class EthnicityUpdate(BaseModel):
    name: Optional[str]
    user_id:Optional[int]
    updated_at: Optional[datetime]