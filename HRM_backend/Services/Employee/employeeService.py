from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from Config.database import get_db
from Models.employeeModel import Employees
from Models.jobPositionModel import JobPosition
from Models.departmentsModel import Departments
from Models.employeeLeaveQuotaModel import EmployeeLeaveQuota
from Models.leaveTypeModel import LeaveType 
from Schema.employeeSchema import EmployeeCreate, EmployeeUpdate
from Services.Register.registerService import UserService
from Models.registersModel import Users
from fastapi.responses import FileResponse
from pathlib import Path
import os
from sqlalchemy import func
import tempfile



class EmployeeService:
    @staticmethod
    # def get_all_employees(db: Session = Depends(get_db)):
    #     return db.query(Employees).all()
    def get_all_employees(db: Session = Depends(get_db)):
        employees = db.query(Employees).all()
        for employee in employees:
            job_position_name = db.query(JobPosition.name).filter(JobPosition.id == employee.job_position_id).scalar()
            department_name = db.query(Departments.name).filter(Departments.id == employee.department_id).scalar()
            employee.job_position_id = job_position_name
            employee.department_id = department_name
        return employees
    
    @staticmethod
    def get_employee_by_id(db: Session, employee_id: int):
        return db.query(Employees).filter(Employees.id == employee_id).first()

    def create_employee(Employee: EmployeeCreate, db: Session = Depends(get_db)):
            # Create the Employees instance
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
                institucion_id=Employee.institucion_id,
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
                active=Employee.active,
                qualification_id=Employee.qualification_id,
                user_id=Employee.user_id,
                the_workouts_selection=Employee.the_workouts_selection,
                created_at=Employee.created_at
            )

            # Add the new employee to the session
            db.add(db_userCreate)
            db.commit()
            db.refresh(db_userCreate)

            # Query all leave types
            leave_types = db.query(LeaveType).all()

            # Assign default leave quotas for the new employee
            for leave_type in leave_types:
                quota = EmployeeLeaveQuota(
                    employee_id=db_userCreate.id,
                    leave_type_id=leave_type.id,
                    amount=leave_type.limit,
                    taken=0.0,
                    available=leave_type.limit,
                    carried_over=0.0,
                    additional_approved=0.0,
                    user_id=Employee.user_id,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None
                )
                db.add(quota)

            db.commit()
            return db_userCreate
    
    @staticmethod
    def update_employee(employee_id: int, Employee: EmployeeUpdate, db: Session = Depends(get_db)):
        db_updateEmployee = db.query(Employees).filter(Employees.id == employee_id).first()
    # def update_employee(employee_id: int, Employee: EmployeeUpdate, db: Session = Depends(get_db)):
    #     db_updateEmployee = db.query(Employees).filter(Employees.id == employee_id).first()

        if db_updateEmployee:

            if Employee.name is not None:
                db_updateEmployee.name = Employee.name
            # if Employee.number is not None:
            #     db_updateEmployee.number = Employee.number
            if Employee.username is not None:
                db_updateEmployee.username = Employee.username
            if Employee.middle_name is not None:
                db_updateEmployee.middle_name = Employee.middle_name
            if Employee.last_name is not None:
                db_updateEmployee.last_name = Employee.last_name
            if Employee.gender is not None:
                db_updateEmployee.gender = Employee.gender
            if Employee.ethnicity_id is not None:
                db_updateEmployee.ethnicity_id = Employee.ethnicity_id
            if Employee.marital_status is not None:
                db_updateEmployee.marital_status = Employee.marital_status
            if Employee.date_hired is not None:
                db_updateEmployee.date_hired = Employee.date_hired
            if Employee.contract_end_date is not None:
                db_updateEmployee.contract_end_date = Employee.contract_end_date
            if Employee.department_id is not None:
                db_updateEmployee.department_id = Employee.department_id
            if Employee.personal_number is not None:
                db_updateEmployee.personal_number = Employee.personal_number
            if Employee.salary is not None:
                db_updateEmployee.salary = Employee.salary
            if Employee.addition is not None:
                db_updateEmployee.addition = Employee.addition
            if Employee.job_position_id is not None:
                db_updateEmployee.job_position_id = Employee.job_position_id
            if Employee.street is not None:
                db_updateEmployee.street = Employee.street
            if Employee.city is not None:
                db_updateEmployee.city = Employee.city
            if Employee.zipcode is not None:
                db_updateEmployee.zipcode = Employee.zipcode
            if Employee.country is not None:
                db_updateEmployee.country = Employee.country
            if Employee.phone_number is not None:
                db_updateEmployee.phone_number = Employee.phone_number
            if Employee.phone_number_2 is not None:
                db_updateEmployee.phone_number_2 = Employee.phone_number_2
            if Employee.email is not None:
                db_updateEmployee.email = Employee.email
            if Employee.email_2 is not None:
                db_updateEmployee.email_2 = Employee.email_2
            if Employee.days_off is not None:
                db_updateEmployee.days_off = Employee.days_off
            if Employee.transferred_days_off is not None:
                db_updateEmployee.transferred_days_off = Employee.transferred_days_off
            if Employee.earned_days_off is not None:
                db_updateEmployee.earned_days_off = Employee.earned_days_off
            if Employee.next_year_earned_days_off is not None:
                db_updateEmployee.next_year_earned_days_off = Employee.next_year_earned_days_off
            if Employee.active is not None:
                db_updateEmployee.active = Employee.active
            if Employee.qualification_id is not None:
                db_updateEmployee.qualification_id = Employee.qualification_id
            if Employee.user_id is not None:
                db_updateEmployee.user_id = Employee.user_id
            if Employee.work_contract_termination_date is not None:
                db_updateEmployee.work_contract_termination_date = Employee.work_contract_termination_date
            if Employee.termination_reason_id is not None:
                db_updateEmployee.termination_reason_id = Employee.termination_reason_id
            if Employee.updated_at is not None:
                db_updateEmployee.updated_at = Employee.updated_at
            if Employee.deleted_at is not None:
                db_updateEmployee.deleted_at = Employee.deleted_at


            db.commit()
            db.refresh(db_updateEmployee)

        return db_updateEmployee
    @staticmethod
    def delete_employee(employee_id: int, db: Session = Depends(get_db)):
        db_employee = db.query(Employees).filter(Employees.id == employee_id).first()

        if db_employee:
            db.delete(db_employee)
            db.commit()

        return db_employee
    @staticmethod
    def get_employee_by_number(db: Session, number: str):
        return db.query(Employees).filter(Employees.number == number).first()

    @staticmethod
    def get_employee_by_personal_number(db: Session, personal_number: str):
        return db.query(Employees).filter(Employees.personal_number == personal_number).first()

    @staticmethod
    def download_cv(employee_id: int, db: Session = Depends(get_db)):
        # Query the database to check if the employee exists
        employee = db.query(Employees).filter(Employees.id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        # Get the employee's CV in binary form from the database
        cv_data = employee.cv
        if not cv_data:
            raise HTTPException(status_code=404, detail="CV file not found")

        try:
            # Create a temporary file to store the CV data
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                temp_file.write(cv_data)
                temp_file_path = temp_file.name

            # Return the temporary file as a response
            return FileResponse(temp_file_path, media_type='application/pdf', filename='employee_cv.pdf')
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error downloading CV: {str(e)}")



    @staticmethod
    def get_last_employee_id(db: Session = Depends(get_db)):
        # Query to get the last employee ID
        last_employee = db.query(Employees).order_by(Employees.id.desc()).first()
        if last_employee:
            return last_employee.id
        else:
            raise HTTPException(status_code=404, detail="No employees found")


    @staticmethod
    def generate_unique_number(db: Session) -> str:
        # Fetch all employee numbers and filter out non-numeric values
        employees = db.query(Employees).all()
        valid_numbers = []
        for employee in employees:
            try:
                valid_numbers.append(int(employee.number))
            except ValueError:
                continue  # Skip invalid numbers

        if valid_numbers:
            new_number = max(valid_numbers) + 1
        else:
            new_number = 1  # Start from 1 if no valid numbers are found

        return f"{new_number:06d}"

    @staticmethod
    def get_total_leave_quota_amount(employee_id: int, db: Session = Depends(get_db)):
        total_amount = db.query(func.sum(EmployeeLeaveQuota.available)).filter(EmployeeLeaveQuota.employee_id == employee_id).scalar()
        return total_amount or 0.0
    # def download_cv(employee_id: int, db: Session = Depends(get_db)):
    #     # Query the database to check if the employee exists
    #     employee = db.query(Employees).filter(Employees.id == employee_id).first()
    #     if not employee:
    #         raise HTTPException(status_code=404, detail="Employee not found")

    #     # Get the employee's CV in binary form from the database
    #     cv_data = employee.cv
    #     if not cv_data:
    #         raise HTTPException(status_code=404, detail="CV file not found")

    #     # Generate a temporary file path
    #     temp_file_path = "DMS/temp_cv.pdf"

    #     # Write the CV data to the temporary file
    #     with open(temp_file_path, "wb") as temp_file:
    #         temp_file.write(cv_data)

    #     # Return the temporary file as a response
    #     return FileResponse(temp_file_path, media_type='application/pdf', filename='employee_cv.pdf')


    
    # @staticmethod
    # def download_cv(employee_id: int, db: Session):
    #         # Query the database to check if the employee exists
    #         employee = db.query(Employees).filter(Employees.id == employee_id).first()
    #         if not employee:
    #             raise HTTPException(status_code=404, detail="Employee not found")

    #         # Get the employee's CV path
    #         cv_path_str = employee.cv.decode() if isinstance(employee.cv, bytes) else str(employee.cv)
    #         cv_path = Path(cv_path_str)
    #         print(cv_path.is_file())
    #         # Check if the file exists
    #         if not cv_path.is_file():
    #             raise HTTPException(status_code=404, detail="CV file not found")

    #         # Return the CV file
    #         return FileResponse(cv_path, media_type='application/pdf', filename='employee_cv.pdf')