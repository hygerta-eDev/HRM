# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime


# class InstitutionCreate(BaseModel):
#     name: str
#     slug: str
#     created_at:datetime
#     user_id:int
#     active:bool

# class InstitutionUpdate(BaseModel):
#     name: Optional[str]
#     slug: Optional[str]
#     user_id:Optional[int]
#     active:bool
#     updated_at: Optional[datetime]

# class InstitutionS(BaseModel):
#     id: int
#     name: str
#     slug: str
#     created_at:datetime
#     updated_at: Optional[datetime]
#     deleted_at:Optional[datetime]
#     user_id:int
#     active:bool



from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InstitutionBase(BaseModel):
    name: str
    slug: str
    user_id: int
    active: bool

class InstitutionCreate(InstitutionBase):
    created_at: datetime

class InstitutionUpdate(InstitutionBase):
    updated_at: Optional[datetime]

class InstitutionResponse(InstitutionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True
