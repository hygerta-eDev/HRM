from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeModel import Employees
from Schema.employeeSchema import EmployeeCreate

class EmployeeService:
    @staticmethod
    def get_all_employees(db: Session = Depends(get_db)):
        return db.query(Employees).all()
    
    def create_employee(Employee: EmployeeCreate, db: Session = Depends(get_db)):
 
        db_userCreate = Employees(
            name=Employee.name,
            number=Employee.number,
            username=Employee.username,
            middle_name=Employee.middle_name,
            last_name=Employee.last_name,
            gender=Employee.gender,
            ethnicity_id=Employee.ethnicity_id,
            marital_status=Employee.marital_status,
            date_of_birth=Employee.date_of_birth,
            date_hired=Employee.date_hired,
            contract_end_date=Employee.contract_end_date,
            department_id=Employee.department_id,
            personal_number=Employee.personal_number,
            salary=Employee.salary,
            addition=Employee.addition,
            job_position_id=Employee.job_position_id,
            street=Employee.street,
            city=Employee.city,
            zipcode=Employee.zipcode,
            country=Employee.country,
            phone_number=Employee.phone_number,
            email=Employee.email,
            email_2=Employee.email_2,
            days_off=Employee.days_off,
            transferred_days_off=Employee.transferred_days_off,
            earned_days_off=Employee.earned_days_off,
            next_year_earned_days_off=Employee.next_year_earned_days_off,
            termination_reason_id=Employee.termination_reason_id,
            # manager_id=Employee.manager_id,
            active=Employee.active,
            qualification_id=Employee.qualification_id,
            user_id=Employee.user_id,

        )

        db.add(db_userCreate)
        db.commit()
        db.refresh(db_userCreate)

        return db_userCreate

   