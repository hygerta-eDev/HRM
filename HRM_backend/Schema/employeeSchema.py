from pydantic import BaseModel, Field
from datetime import date
from typing import Optional,List
from datetime import datetime
from .enums.genders import Genders
from .enums.Marital_status import MaritalStatus


class EmployeeBase(BaseModel):

    name: Optional[str]
    number: Optional[str]
    username: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    gender: Genders 
    ethnicity_id: Optional[int]
    marital_status: Optional[MaritalStatus]
    # driving_license: str
    date_of_birth: Optional[date]
    date_hired: Optional[date]
    contract_end_date: Optional[date]
    institucion_id: Optional[int]
    department_id: Optional[int]
    personal_number: Optional[str] = Field(..., unique=True, index=True)
    salary: Optional[str] = '0'
    # salary_coefficient: str = '0'
    addition: Optional[int] = 0
    job_position_id: Optional[int]
    street: Optional[str]
    city: Optional[str]
    zipcode: Optional[str]
    country: Optional[str]
    phone_number: Optional[str]
    phone_number_2: Optional[str]
    email: Optional[str]
    email_2: Optional[str]
    days_off: Optional[int] = 0
    transferred_days_off: Optional[int] = 0
    earned_days_off: Optional[int] = 0
    next_year_earned_days_off: Optional[int] = 2028
    # manager_id: Optional[int]
    active: Optional[bool] = True
    qualification_id: Optional[int]
    user_id: Optional[int]
    # bank_account: str
    # bank_id: int
    # cv: Optional[bytes]
    # documents: Optional[List[bytes]] = None  # Fix array declaration
    the_workouts_selection:Optional[str]



class EmployeeCreate(EmployeeBase):
    created_at:datetime


# class EmployeeUpdate(EmployeeBase):
#     work_contract_termination_date: Optional[date] = None
#     termination_reason_id: Optional[int] = None
#     updated_at:datetime
#     deleted_at:datetime

class EmployeeUpdate(BaseModel):
    name: Optional[str]
    number: Optional[str]
    username: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Genders]
    ethnicity_id: Optional[int]
    marital_status: Optional[MaritalStatus]
    date_of_birth: Optional[date]
    date_hired: Optional[date]
    contract_end_date: Optional[date]
    department_id: Optional[int]
    personal_number: Optional[str]
    salary: Optional[str]
    addition: Optional[int]
    job_position_id: Optional[int]
    street: Optional[str]
    city: Optional[str]
    zipcode: Optional[str]
    country: Optional[str]
    phone_number: Optional[str]
    phone_number_2: Optional[str]
    email: Optional[str]
    email_2: Optional[str]
    days_off: Optional[int]
    transferred_days_off: Optional[int]
    earned_days_off: Optional[int]
    next_year_earned_days_off: Optional[int]
    active: Optional[bool]
    qualification_id: Optional[int]
    user_id: Optional[int]
    work_contract_termination_date: Optional[date]
    termination_reason_id: Optional[int]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    class Config:
        from_attributes = True
        
class UsernameRequest(BaseModel):
    name: str
    last_name: str

class UsernameResponse(BaseModel):
    username: str