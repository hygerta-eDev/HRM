from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EmployeeLeaveQuotaCreate(BaseModel):
    leave_type_id: int
    employee_id: int
    leave_period_id: int
    amount: float
    taken: float
    available: float
    carried_over: float
    additional_approved: float
    user_id:int
    created_at :datetime
class EmployeeLeaveQuotaCall(BaseModel):
    leave_type_id: int
    employee_id: int
    # leave_period_id: int
    amount: float
    taken: float
    available: float
    carried_over: float
    additional_approved: float
    user_id:int
    created_at :datetime

class EmployeeLeaveQuotaUpdate(BaseModel):
    leave_type_id: Optional[int]
    employee_id: Optional[int]
    leave_period_id: Optional[int]
    amount: Optional[float]
    taken: Optional[float]
    available: Optional[float]
    carried_over: Optional[float]
    additional_approved: Optional[float]
    user_id:Optional[int]
    updated_at :Optional[datetime]
