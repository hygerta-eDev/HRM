from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .assessmentService import AssessmentService
from Schema.assesmentSchema import AssessmentCreate
from Config.database import get_db

router = APIRouter(prefix="/assessment", tags=["Assessment"])

@router.get("/")
def get_all_assessment(db: Session = Depends(get_db)):
    return AssessmentService.get_all_assessment(db=db)

@router.post("/create_assessment")
def create_assessment(Assessments: AssessmentCreate, db: Session = Depends(get_db)):
    return AssessmentService.create_assessment(Assessments, db)

