from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .institutionsService import InstitutionService
from Schema.institutionsSchema import InstitutionCreate,InstitutionUpdate
from Config.database import get_db
from Models.departmentsModel import Departments
from Models.jobPositionModel import JobPosition
from typing import List

router = APIRouter(prefix="/institutions", tags=["Institutions"])

@router.get("/")
def get_all_institutions(db: Session = Depends(get_db)):
    return InstitutionService.get_all_institutions(db=db)

@router.get("/active_institutions")
def get_all_active_institutions(db: Session = Depends(get_db)):
    return InstitutionService.get_all_active_institutions(db=db)

@router.get("/{institution_id}")
def get_institution(institution_id: int, db: Session = Depends(get_db)):
    institution = InstitutionService.get_institution_by_id(db, institution_id)
    if institution is None:
        raise HTTPException(status_code=404, detail="institution not found")
    return institution


@router.post("/create_institution")
def create_institutions(Institutions: InstitutionCreate, db: Session = Depends(get_db)):
    return InstitutionService.create_institutions(Institutions, db)

@router.put("/update_institutions/{institution_id}")
def update_institutions(institution_id: int, institucion: InstitutionUpdate, db: Session = Depends(get_db)):
    institution=InstitutionService.update_institutions(institution_id=institution_id, institucion=institucion, db=db)
    if institution is None:
        raise HTTPException(status_code=404, detail="Institution not found or has been soft-deleted")
    return institution

@router.delete("/delete_institution/{institution_id}")
def delete_institution(institution_id: int, db: Session = Depends(get_db)):
    return InstitutionService.delete_institution(institution_id=institution_id, db=db)


@router.get("/job_positions/{institution_id}/{department_id}")
def get_job_positions_for_department(institutions_id: int, department_id: int, db: Session = Depends(get_db)):
    job_positions = db.query(JobPosition).\
        join(Departments, JobPosition.department_id == Departments.id).\
        filter(Departments.institution_id == institutions_id).\
        filter(Departments.id == department_id).\
        all()

    if not job_positions:
        raise HTTPException(status_code=404, detail="Job positions not found")

    return job_positions
# # @app.get("/departments/{department_id}/job_positions/", response_model=DepartmentJobPositions)
# @router.get("/{department_id}/job_positions/")
# def get_department_job_positions(department_id: int, db: Session = Depends(get_db)):
#     return DepartmentService.get_department_job_positions(department_id=department_id, db=db)