from pydantic import BaseModel
from datetime import datetime

class EmployeeLeaveQuotaSchema(BaseModel):
    leave_type_id: int
    employee_id: int
    leave_period_id: int
    amount: float
    taken: float
    available: float
    carried_over: float
    additional_approved: float
    created_at :datetime
    updated_at :datetime
    deleted_at :datetime