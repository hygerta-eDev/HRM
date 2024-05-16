from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EmployeeRolesBase(BaseModel):
    employee_id: Optional[int]
    role_id: Optional[int]
    expires_at: Optional[datetime] 
    user_id: int
    created_at: Optional[datetime]
    # updated_at: Optional[datetime]
    # deleted_at: Optional[datetime]

class EmployeeRolesCreate(EmployeeRolesBase):
    pass

class EmployeeRolesUpdate(EmployeeRolesBase):
    pass

class EmployeeRolesInDBBase(EmployeeRolesBase):
    id: int

    class Config:
        orm_mode = True

class EmployeeRoles(EmployeeRolesInDBBase):
    pass
