from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .employeeService import EmployeeService
from Schema.employeeSchema import EmployeeCreate
from Config.database import get_db

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.get("/")
def get_all_employees(db: Session = Depends(get_db)):
    return EmployeeService.get_all_employees(db=db)

@router.post("/create_employee")
def create_employee(Employee: EmployeeCreate, db: Session = Depends(get_db)):
    return EmployeeService.create_employee(Employee, db)

