from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .testservice import TestService
from Schema.test import CreateDepartmentSchema
from Config.database import get_db

router = APIRouter(prefix="/departments", tags=["Departments"])

# @router.get("/")
# def get_all_departments(db: Session = Depends(get_db)):
#     return TestService.get_all_departments(db=db)

# @router.post("/")
# def create_department(department: CreateDepartmentSchema, db: Session = Depends(get_db)):
#     return TestService.create_department(department, db)

