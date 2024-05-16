from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .employee_qualificationService import QualificationService
from Schema.employee_qualificationSchema import QualificationCreate, QualificationUpdate
from Config.database import get_db

router = APIRouter(prefix="/qualification", tags=["Qualification"])

@router.get("/")
def get_all_qualifications(db: Session = Depends(get_db)):
    return QualificationService.get_all_qualifications(db=db)

@router.get("/active_qualifications")
def get_all_active_qualifications(db: Session = Depends(get_db)):
    return QualificationService.get_all_active_qualifications(db=db)

@router.get("/{qualification_id}")
def get_department(qualification_id: int, db: Session = Depends(get_db)):
    qualification = QualificationService.get_qualification_by_id(db, qualification_id)
    if qualification is None:
        raise HTTPException(status_code=404, detail="qualification not found")
    return qualification

@router.post("/create_qualifications")
def create_qualifications(Qualifications: QualificationCreate, db: Session = Depends(get_db)):
    return QualificationService.create_qualifications(Qualifications, db)

@router.put("/update_qualifications/{qualification_id}")
def update_qualifications(qualification_id: int, qualification: QualificationUpdate, db: Session = Depends(get_db)):
    qualification =  QualificationService.update_qualifications(qualification_id=qualification_id, qualification=qualification, db=db)
    if qualification is None:
        raise HTTPException(status_code=404, detail="qualification not found or has been soft-deleted")
    return qualification

@router.delete("/delete_qualification/{qualification_id}")
def delete_qualification(qualification_id: int, db: Session = Depends(get_db)):
    return QualificationService.delete_qualification(qualification_id=qualification_id, db=db)
