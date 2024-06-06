from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.employeeRolesModels import EmployeeRoles
from Models.employeeModel import Employees
from Models.rolesModel import Roles
from Models.departmentsModel import Departments 

from Schema.employee_rolesSchema import EmployeeRolesCreate

class EmployeeRolesService:
    @staticmethod
    def get_all_employeeRoles(db: Session = Depends(get_db)):
        return db.query(EmployeeRoles).all()
    # @staticmethod
    # def get_leaveType_by_id(db: Session, leaveType_id: int):
    #     return db.query(EmployeeRoles).filter(EmployeeRoles.id == leaveType_id).first()
   
    def create_employeeRoles(EmployeeRole: EmployeeRolesCreate, db: Session = Depends(get_db)):
 
        db_employeeRoles = EmployeeRoles(
            employee_id=EmployeeRole.employee_id,
            role_id=EmployeeRole.role_id,
            expires_at=EmployeeRole.expires_at,
            user_id=EmployeeRole.user_id,
            created_at=EmployeeRole.created_at,
            # updated_at=LeaveTypes.updated_at,
            # deleted_at=LeaveTypes.deleted_at,
            
        )

        db.add(db_employeeRoles)
        db.commit()
        db.refresh(db_employeeRoles)

        return db_employeeRoles
    

    @staticmethod
    def get_all_employees_by_role(role_name: str, db: Session = Depends(get_db)):
        # Query employees based on the role name
        employees_with_role = (
            db.query(Employees)
            .join(EmployeeRoles)
            .join(Roles)
            .filter(Roles.name == role_name)
            .all()
        )
        return employees_with_role
    
    def get_role_manager_by_department(department_name: str, role_name: str, db: Session):
    # Assuming your Employees table has a department_id column
    # If not, adjust the join condition accordingly
        # Join Employees with EmployeeRoles, Roles, and potentially Departments (if needed)
        query = (
            db.query(Employees)
            .join(EmployeeRoles)
            .join(Roles)
            .join(Departments)  # Join with Departments if the department information is stored there
            .filter(Roles.name == role_name)
            .filter(Departments.name == department_name)
            .filter(EmployeeRoles.employee_id == Employees.id)  # Assuming a join condition between EmployeeRoles and Employees
            .all()
        )

    # Now you have a list of employees who are managers of the specified role in the given department
        return query

    # @staticmethod
    # def update_leaveType(leaveType_id: int, leaveType: LeaveTypeUpdate, db: Session = Depends(get_db)):
    #     db_leaveType = db.query(LeaveType).filter(LeaveType.id == leaveType_id).first()

    #     if db_leaveType:
    #         if db_leaveType.limit is not None:
    #             db_leaveType.limit = leaveType.limit
    #         if db_leaveType.slug is not None:
    #             db_leaveType.slug = leaveType.slug
    #         if db_leaveType.updated_at is not None:
    #             db_leaveType.updated_at = leaveType.updated_at
    #         if db_leaveType.deleted_at is not None:
    #             db_leaveType.deleted_at = leaveType.deleted_at


    #         db.commit()
    #         db.refresh(db_leaveType)

    #     return db_leaveType
    # @staticmethod
    # def delete_department(leaveType_id: int, db: Session = Depends(get_db)):
    #     db_leaveType = db.query(LeaveType).filter(LeaveType.id == leaveType_id).first()

    #     if db_leaveType:
    #         db.delete(db_leaveType)
    #         db.commit()

    #     return db_leaveType
   