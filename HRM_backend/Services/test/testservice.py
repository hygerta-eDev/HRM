from fastapi import Depends
from sqlalchemy.orm import Session
from Config.database import get_db

from Models.test import Test
from Schema.test import CreateDepartmentSchema

class TestService:
    @staticmethod
    def get_all_departments(db: Session = Depends(get_db)):
        return db.query(Test).all()
    
    @staticmethod
    def get_departmentss(department_id: int, db: Session = Depends(get_db)):
        return db.query(Test).filter_by(department_id=department_id).first()


    @staticmethod
    def create_departmentssx(department: CreateDepartmentSchema, db: Session = Depends(get_db)):
        db_test = Test(
            name=department.name,
            description=department.description,
        )

        db.add(db_test)
        db.commit()
        db.refresh(db_test)

        return db_test

