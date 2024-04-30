from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .employee_qualificationService import QualificationService
from Schema.employee_qualificationSchema import QualificationCreate
from Config.database import get_db

router = APIRouter(prefix="/qualification", tags=["Qualification"])

@router.get("/")
def get_all_qualifications(db: Session = Depends(get_db)):
    return QualificationService.get_all_qualifications(db=db)

@router.post("/create_department")
def create_qualifications(Qualifications: QualificationCreate, db: Session = Depends(get_db)):
    return QualificationService.create_qualifications(Qualifications, db)

