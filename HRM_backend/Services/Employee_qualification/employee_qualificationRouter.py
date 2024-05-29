from fastapi import APIRouter, Depends, HTTPException, Form,Request
from sqlalchemy.orm import Session
from .employee_qualificationService import QualificationService
from Models.employeeQualificationModel import Qualification 
from Schema.employee_qualificationSchema import QualificationCreate, QualificationUpdate,QualificationSchema
from Config.database import get_db
from typing import List

router = APIRouter(prefix="/qualification", tags=["Qualification"])

@router.get("/",response_model=List[QualificationSchema])
def get_all_qualifications(db: Session = Depends(get_db)):
    return QualificationService.get_all_qualifications(db=db)

@router.get("/active_qualifications",response_model=List[QualificationSchema])
def get_all_active_qualifications(db: Session = Depends(get_db)):
    return QualificationService.get_all_active_qualifications(db=db)

@router.get("/{qualification_id}",response_model=QualificationSchema)
def get_department(qualification_id: int, db: Session = Depends(get_db)):
    qualification = QualificationService.get_qualification_by_id(db, qualification_id)
    if qualification is None:
        raise HTTPException(status_code=404, detail="qualification not found")
    return qualification

@router.post("/create_qualifications",response_model=QualificationSchema)
def create_qualifications(Qualifications: QualificationCreate, db: Session = Depends(get_db)):
    return QualificationService.create_qualifications(Qualifications, db)

@router.put("/update_qualifications/{qualification_id}",response_model=QualificationSchema)
def update_qualifications(qualification_id: int, qualification: QualificationUpdate, request: Request, db: Session = Depends(get_db)):
    user_id = int(request.headers.get('X-User-Id', 1))
    entity_id = qualification_id
    entity_type = Qualification
    updated_qualification = QualificationService.update_qualifications(qualification_id=qualification_id, qualification=qualification, entity_id=entity_id, entity_type=entity_type, db=db, user_id=user_id)
    if updated_qualification is None:
        raise HTTPException(status_code=404, detail="Qualification not found or has been soft-deleted")
    return updated_qualification


@router.delete("/delete_qualification/{qualification_id}",response_model=QualificationSchema)
def delete_qualification(qualification_id: int, db: Session = Depends(get_db)):
    return QualificationService.delete_qualification(entity_id=qualification_id, db=db)
