from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeModel import Employees
from Schema.employeeSchema import EmployeeCreate, EmployeeUpdate
from Services.Register.registerService import UserService
from Models.registersModel import Users

class EmployeeService:
    @staticmethod
    def get_all_employees(db: Session = Depends(get_db)):
        return db.query(Employees).all()
    @staticmethod
    def get_employee_by_id(db: Session, employee_id: int):
        return db.query(Employees).filter(Employees.id == employee_id).first()
    
    def create_employee(Employee: EmployeeCreate, db: Session = Depends(get_db)):
    #    print(current_user)
    #    current_user: Users = Depends(UserService.get_current_user)
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
            # termination_reason_id=Employee.termination_reason_id,
            # manager_id=Employee.manager_id,
            active=Employee.active,
            qualification_id=Employee.qualification_id,
            user_id=Employee.user_id,
            created_at = Employee.created_at

        )

        db.add(db_userCreate)
        db.commit()
        db.refresh(db_userCreate)
        return db_userCreate
    
    # @staticmethod
    # def update_appointment(employee_id: int, Employee: EmployeeUpdate, db: Session = Depends(get_db)):
    #     db_updateEmployee = db.query(Employees).filter(Employees.id == employee_id).first()

    #     if db_updateEmployee:

    #         if Employee.name is not None:
    #             db_updateEmployee.name = Employee.name
    #         if Employee.number is not None:
    #             db_updateEmployee.number = Employee.number
    #         if Employee.username is not None:
    #             db_updateEmployee.username = Employee.username
    #         if Employee.middle_name is not None:
    #             db_updateEmployee.middle_name = Employee.middle_name
    #         if Employee.last_name is not None:
    #             db_updateEmployee.last_name = Employee.last_name
    #         if Employee.gender is not None:
    #             db_updateEmployee.gender = Employee.gender
    #         if Employee.ethnicity_id is not None:
    #             db_updateEmployee.ethnicity_id = Employee.ethnicity_id
    #         if Employee.marital_status is not None:
    #             db_updateEmployee.marital_status = Employee.marital_status
    #         if Employee.date_hired is not None:
    #             db_updateEmployee.date_hired = Employee.date_hired
    #         if Employee.contract_end_date is not None:
    #             db_updateEmployee.contract_end_date = Employee.contract_end_date
    #         if Employee.department_id is not None:
    #             db_updateEmployee.department_id = Employee.department_id
    #         if Employee.personal_number is not None:
    #             db_updateEmployee.personal_number = Employee.personal_number
    #         if Employee.salary is not None:
    #             db_updateEmployee.salary = Employee.salary
    #         if Employee.addition is not None:
    #             db_updateEmployee.addition = Employee.addition
    #         if Employee.job_position_id is not None:
    #             db_updateEmployee.job_position_id = Employee.job_position_id
    #         if Employee.street is not None:
    #             db_updateEmployee.street = Employee.street
    #         if Employee.city is not None:
    #             db_updateEmployee.city = Employee.city
    #         if Employee.zipcode is not None:
    #             db_updateEmployee.zipcode = Employee.zipcode
    #         if Employee.country is not None:
    #             db_updateEmployee.country = Employee.country
    #         if Employee.phone_number is not None:
    #             db_updateEmployee.phone_number = Employee.phone_number
    #         if Employee.phone_number_2 is not None:
    #             db_updateEmployee.phone_number_2 = Employee.phone_number_2
    #         if Employee.email is not None:
    #             db_updateEmployee.email = Employee.email
    #         if Employee.email_2 is not None:
    #             db_updateEmployee.email_2 = Employee.email_2
    #         if Employee.days_off is not None:
    #             db_updateEmployee.days_off = Employee.days_off
    #         if Employee.transferred_days_off is not None:
    #             db_updateEmployee.transferred_days_off = Employee.transferred_days_off
    #         if Employee.earned_days_off is not None:
    #             db_updateEmployee.earned_days_off = Employee.earned_days_off
    #         if Employee.next_year_earned_days_off is not None:
    #             db_updateEmployee.next_year_earned_days_off = Employee.next_year_earned_days_off
    #         if Employee.active is not None:
    #             db_updateEmployee.active = Employee.active
    #         if Employee.qualification_id is not None:
    #             db_updateEmployee.qualification_id = Employee.qualification_id
    #         if Employee.user_id is not None:
    #             db_updateEmployee.user_id = Employee.user_id
    #         if Employee.work_contract_termination_date is not None:
    #             db_updateEmployee.work_contract_termination_date = Employee.work_contract_termination_date
    #         if Employee.termination_reason_id is not None:
    #             db_updateEmployee.termination_reason_id = Employee.termination_reason_id
    #         if Employee.updated_at is not None:
    #             db_updateEmployee.updated_at = Employee.updated_at
    #         if Employee.deleted_at is not None:
    #             db_updateEmployee.deleted_at = Employee.deleted_at


    #         db.commit()
    #         db.refresh(db_updateEmployee)

    #     return db_updateEmployee

   