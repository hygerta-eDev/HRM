from pydantic import BaseModel
from typing import Optional

class DepartmentCreate(BaseModel):
    name: str
    slug: str
    # ethnicity_id:Optional[int]
class DepartmentUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    # ethnicity_id:Optional[int]
