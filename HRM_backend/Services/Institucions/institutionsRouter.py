from fastapi import APIRouter, Depends, HTTPException, Form,Request,Header
from sqlalchemy.orm import Session
from .institutionsService import InstitutionService
from Schema.institutionsSchema import InstitutionCreate,InstitutionUpdate,InstitutionResponse
from Config.database import get_db
from Models.departmentsModel import Departments
from Models.jobPositionModel import JobPosition
from Models.institutionModel import Institution
from ..Register.registerService import UserService

from typing import List

router = APIRouter(prefix="/institutions", tags=["Institutions"])
@router.get("/debug")
def debug_headers(x_user_id: str = Header(None)):
    return {"x_user_id": x_user_id}
@router.get("/", response_model=List[InstitutionResponse])
def get_all_institutions(
    db: Session = Depends(get_db),
    user_id: int = Depends(UserService.get_user_id_from_header)  # Dependency for user_id
):
    return InstitutionService.get_all_institutions(db=db, user_id=user_id)

@router.get("/active_institutions",response_model=List[InstitutionResponse])
def get_all_active_institutions(db: Session = Depends(get_db),    user_id: int = Depends(UserService.get_user_id_from_header)):
    return InstitutionService.get_all_active_institutions(db=db,user_id=user_id)


@router.get("/{institution_id}", response_model=InstitutionResponse)
def get_department(institution_id: int, db: Session = Depends(get_db)):
    return InstitutionService.get_institution_by_id(db=db, entity_id=institution_id)

# @router.get("/{institution_id}", response_model=InstitutionResponse)
# def get_institution_by_id(institution_id: int, db: Session = Depends(get_db)):
#     institution = InstitutionService.get_institution_by_id(db=db, entity_id=institution_id)
#     if institution is None:
#         raise HTTPException(status_code=404, detail="institution not found")
#     return institution

@router.post("/create_institution", response_model=InstitutionResponse)
def create_institution(InstitutionData: InstitutionCreate, request: Request, db: Session = Depends(get_db)):
    return InstitutionService.create_institutions(InstitutionData, db)

@router.put("/{institution_id}", response_model=InstitutionResponse)
def update_institution(institution_id: int, institution_data: InstitutionUpdate, request: Request, db: Session = Depends(get_db)):
    user_id = int(request.headers.get('X-User-Id', 1))
    entity_id = institution_id
    entity_type = Institution
    return InstitutionService.update_institution(institution_id, institution_data, entity_id=entity_id, entity_type=entity_type, db=db, user_id=user_id)

@router.delete("/delete_institution/{institution_id}",response_model=InstitutionResponse)
def delete_institution(institution_id: int, db: Session = Depends(get_db)):
    return InstitutionService.delete_institution(entity_id=institution_id, db=db)


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