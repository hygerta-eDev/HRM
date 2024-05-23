from fastapi import APIRouter, Depends, HTTPException, Form,Request
from sqlalchemy.orm import Session
from .departmentsService import DepartmentService
from Schema.departmentsSchema import DepartmentCreate,DepartmentUpdate,Department
from Models.departmentsModel import Departments
from Config.database import get_db
from typing import List

router = APIRouter(prefix="/departments", tags=["Departments"])

# @router.get("/")
# def get_all_departments(db: Session = Depends(get_db)):
#     return DepartmentService.get_all_departments(db=db)

@router.get("/", response_model=List[Department])
def get_all_departments(db: Session = Depends(get_db),user_id: int = None):
    departments = DepartmentService.get_all_departments(db=db)
    if not departments:
        raise HTTPException(status_code=404, detail="No departments found")
    return departments

@router.get("/active_departments",  response_model=List[Department])
def get_all_active_departments(db: Session = Depends(get_db)):
    return DepartmentService.get_all_active_departments(db=db)


# @router.get("/{department_id}", response_model=Department)
# def get_department_by_id(department_id: int, db: Session = Depends(get_db)):
#     department = DepartmentService.get_department_by_id(db=db, entity_id=department_id)
#     if department is None:
#         raise HTTPException(status_code=404, detail="Department not found")
#     return department

@router.get("/{department_id}", response_model=Department)
def get_department(department_id: int, db: Session = Depends(get_db)):
    return DepartmentService.get_department_by_id(db=db, entity_id=department_id)

@router.post("/create_department",response_model=DepartmentCreate)
def create_departments(Department: DepartmentCreate, db: Session = Depends(get_db)):
    return DepartmentService.create_departments(Department, db)

@router.put("/update_department/{department_id}", response_model=DepartmentUpdate)
def update_department(department_id: int, department: DepartmentUpdate, request: Request, db: Session = Depends(get_db)):
    entity_id = department_id
    entity_type = Departments
    return DepartmentService.update_department(department_id=department_id, entity_id=entity_id, entity_type=entity_type, department=department, db=db)

@router.delete("/delete_department/{department_id}", response_model=Department)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    return DepartmentService.delete_department(entity_id=department_id, db=db)

# @app.get("/departments/{department_id}/job_positions/", response_model=DepartmentJobPositions)
@router.get("/{department_id}/job_positions/")
def get_department_job_positions(department_id: int, db: Session = Depends(get_db)):
    return DepartmentService.get_department_job_positions(department_id=department_id, db=db)