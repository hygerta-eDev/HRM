from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.departmentsModel import Departments
from Models.ethnicitiesModel import Ethnicities

from Schema.departmentsSchema import DepartmentCreate


class DepartmentService:
    @staticmethod
    def get_all_departments(db: Session = Depends(get_db)):
        return db.query(Departments).all()
    
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
