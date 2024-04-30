from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class EmployeeCreate(BaseModel):
    name: Optional[str]
    number: Optional[str]
    username: str
    middle_name: str
    last_name: str
    gender: str = 'N/A'
    ethnicity_id: int
    marital_status: str = 'single'
    # driving_license: str
    date_of_birth: date
    date_hired: date
    contract_end_date: date
    department_id: Optional[int]
    personal_number: str = Field(..., unique=True, index=True)
    salary: str = '0'
    # salary_coefficient: str = '0'
    addition: int = 0
    job_position_id: Optional[int]
    street: str
    city: str
    zipcode: str
    country: str
    phone_number: str
    phone_number_2: str
    email: str
    email_2: str
    days_off: int = 0
    transferred_days_off: int = 0
    earned_days_off: int = 0
    next_year_earned_days_off: int = 2028
    work_contract_termination_date: Optional[date] = None
    termination_reason_id: Optional[int]
    # manager_id: Optional[int]
    active: bool = True
    qualification_id: Optional[int]
    user_id: int
    # bank_account: str
    # bank_id: int
