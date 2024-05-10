from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .departmentsService import DepartmentService
from Schema.departmentsSchema import DepartmentCreate,DepartmentUpdate
from Config.database import get_db

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.get("/")
def get_all_departments(db: Session = Depends(get_db)):
    return DepartmentService.get_all_departments(db=db)

@router.get("/{department_id}")
def get_department(department_id: int, db: Session = Depends(get_db)):
    department = DepartmentService.get_department_by_id(db, department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


@router.post("/create_department")
def create_departments(Department: DepartmentCreate, db: Session = Depends(get_db)):
    return DepartmentService.create_departments(Department, db)

@router.put("/update_department/{department_id}")
def update_department(department_id: int, department: DepartmentUpdate, db: Session = Depends(get_db)):
    return DepartmentService.update_department(department_id=department_id, department=department, db=db)

@router.delete("/delete_department/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):
    return DepartmentService.delete_department(department_id=department_id, db=db)

# @app.get("/departments/{department_id}/job_positions/", response_model=DepartmentJobPositions)
@router.get("/{department_id}/job_positions/")
def get_department_job_positions(department_id: int, db: Session = Depends(get_db)):
    return DepartmentService.get_department_job_positions(department_id=department_id, db=db)