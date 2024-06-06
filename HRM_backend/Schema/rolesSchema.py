from pydantic import BaseModel, constr, validator
from datetime import datetime
from Config.database import get_db
from typing import Optional

class RolesCreate(BaseModel):
    name: str