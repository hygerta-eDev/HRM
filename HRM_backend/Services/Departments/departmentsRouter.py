from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .departmentsService import DepartmentService
from Schema.departmentsSchema import DepartmentCreate
from Config.database import get_db

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.get("/")
def get_all_department(db: Session = Depends(get_db)):
    return DepartmentService.get_all_department(db=db)

@router.post("/create_department")
def create_departments(Department: DepartmentCreate, db: Session = Depends(get_db)):
    return DepartmentService.create_departments(Department, db)

