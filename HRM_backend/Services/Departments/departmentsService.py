from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.departmentsModel import Departments
from Models.ethnicitiesModel import Ethnicities

from Schema.departmentsSchema import DepartmentCreate, DepartmentUpdate


class DepartmentService:
    @staticmethod
    def get_all_departments(db: Session = Depends(get_db)):
        return db.query(Departments).all()
    
    @staticmethod
    def get_department_by_id(db: Session, department_id: int):
        return db.query(Departments).filter(Departments.id == department_id).first()
    

    def create_departments(Department: DepartmentCreate, db: Session = Depends(get_db)):

        db_departments = Departments(
            name=Department.name,
            slug = Department.slug,
            # manager_id=Department.manager_id
            # ethnicity_id=Department.ethnicity_id

        )

        db.add(db_departments)
        db.commit()
        db.refresh(db_departments)

        return db_departments
    @staticmethod
    def update_department(department_id: int, department: DepartmentUpdate, db: Session = Depends(get_db)):
        db_department = db.query(Departments).filter(Departments.id == department_id).first()

        if db_department:
            if department.name is not None:
                db_department.name = department.name
            if db_department.slug is not None:
                db_department.slug = department.slug

            db.commit()
            db.refresh(db_department)

        return db_department
    @staticmethod
    def delete_department(department_id: int, db: Session = Depends(get_db)):
        db_department = db.query(Departments).filter(Departments.id == department_id).first()

        if db_department:
            db.delete(db_department)
            db.commit()

        return db_department