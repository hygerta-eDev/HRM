from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.departmentsModel import Departments
from Models.ethnicitiesModel import Ethnicities
from Config.logging_utils import log_function_call
from sqlalchemy import func

from Schema.departmentsSchema import DepartmentCreate, DepartmentUpdate


class DepartmentService:
    @staticmethod
    @log_function_call(entity_name="Department")
    # @log_function_call
    def get_all_departments(db: Session,user_id: int = None):
        return db.query(Departments).all()
    
    @staticmethod
    @log_function_call(entity_name="Department")
    def get_all_active_departments(db: Session, user_id: int):
        # Log or use user_id as needed
        return db.query(Departments).filter(Departments.deleted_at == None).all()

    @staticmethod
    @log_function_call(entity_name="Department")
    # @log_function_call
    def get_department_by_id(db: Session, entity_id: int):
        return db.query(Departments).filter(Departments.id == entity_id).first()
    

    @staticmethod
    @log_function_call(entity_name="Department")
    def create_departments(Department: DepartmentCreate, db: Session) -> DepartmentCreate:
        db_departments = Departments(
            name=Department.name,
            slug=Department.slug,
            institution_id=Department.institution_id,
            user_id=Department.user_id,
            active=Department.active,

            # created_at=Department.created_at
        )

        db.add(db_departments)
        db_departments.created_at = func.now()
        db.commit()
        db.refresh(db_departments)

        return db_departments
    
    @staticmethod
    @log_function_call(entity_name="Department")
    def update_department(department_id: int, entity_id: int, entity_type: type, department: DepartmentUpdate, db: Session) -> DepartmentUpdate:
        db_department = db.query(entity_type).filter(entity_type.id == entity_id).first()

        if not db_department:
            raise HTTPException(status_code=404, detail="Department not found")

        for key, value in department.dict().items():
            setattr(db_department, key, value)
        db_department.updated_at = func.now()

        db.commit()

        db.refresh(db_department)

        return db_department

    @staticmethod
    @log_function_call(entity_name="Department")
    def delete_department(entity_id: int, db: Session = Depends(get_db)):
        db_department = db.query(Departments).filter(Departments.id == entity_id).first()

        if db_department:
            db_department.soft_delete()  
            # db.delete(db_department)
            db.commit()

        return db_department
    
    @staticmethod
    # @log_function_call
    def get_department_job_positions(department_id: int, db: Session = Depends(get_db)):
        department = db.query(Departments).filter(Departments.id == department_id).first()
        if department is None:
            raise HTTPException(status_code=404, detail="Department not found")
        job_positions = department.job_positions
        return {"department_id": department_id, "job_positions": job_positions}
