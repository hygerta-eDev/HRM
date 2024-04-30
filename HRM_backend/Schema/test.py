from pydantic import BaseModel
from typing import Optional

class CreateDepartmentSchema(BaseModel):
    name: str
    description: str

