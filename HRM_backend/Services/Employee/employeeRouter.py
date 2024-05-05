from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .employeeService import EmployeeService
from Schema.employeeSchema import EmployeeCreate,EmployeeUpdate
from Config.database import get_db

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.get("/")
def get_all_employees(db: Session = Depends(get_db)):
    return EmployeeService.get_all_employees(db=db)

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = EmployeeService.get_employee_by_id(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.post("/create_employee")
def create_employee(Employee: EmployeeCreate, db: Session = Depends(get_db)):
    return EmployeeService.create_employee(Employee, db)

# @router.put("/employees/{employee_id}/update_appointment")
# def update_employee_appointment(employee_id: int, employee_update: EmployeeUpdate, db: Session = Depends(get_db)):
#     updated_employee = EmployeeService.update_appointment(employee_id=employee_id, Employee=employee_update, db=db)
#     if not updated_employee:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return updated_employee
@router.put("/{employee_id}")
def update_appointment(employee_id: int, Employee: EmployeeUpdate, db: Session = Depends(get_db)):
    return EmployeeService.update_appointment(employee_id=employee_id, Employee=Employee, db=db)
@router.put("/employees/{employee_id}/update_appointment")
def update_employee_appointment(employee_id: int, employee_update: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = EmployeeService.get_employee_by_id(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Update only the fields that are provided in the request
    for field, value in employee_update.dict().items():
        if value is not None:
            setattr(db_employee, field, value)
    
    db.commit()
    db.refresh(db_employee)
    
    return db_employee