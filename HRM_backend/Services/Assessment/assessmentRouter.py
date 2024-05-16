from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .assessmentService import AssessmentService
from Schema.assesmentSchema import AssessmentCreate,AssessmentUpdate
from Config.database import get_db

router = APIRouter(prefix="/assessment", tags=["Assessment"])

@router.get("/")
def get_all_assessments(db: Session = Depends(get_db)):
    return AssessmentService.get_all_assessments(db=db)

@router.get("/active_assessments")
def get_all_active_assessments(db: Session = Depends(get_db)):
    return AssessmentService.get_all_active_assessments(db=db)

@router.get("/{assessment_id}")
def get_assessment_by_id(assessment_id: int, db: Session = Depends(get_db)):
    assessment = AssessmentService.get_assessment_by_id(db, assessment_id)
    if assessment is None:
        raise HTTPException(status_code=404, detail="assessment not found")
    return assessment

@router.post("/create_assessment")
def create_assessment(Assessments: AssessmentCreate, db: Session = Depends(get_db)):
    return AssessmentService.create_assessment(Assessments, db)

@router.put("/update_assessments/{assessment_id}")
def update_assessments(assessment_id: int, assessment: AssessmentUpdate, db: Session = Depends(get_db)):
    assessment=AssessmentService.update_assessments(assessment_id=assessment_id, assessment=assessment, db=db)
    if assessment is None:
        raise HTTPException(status_code=404, detail="assessment not found or has been soft-deleted")
    return assessment

@router.delete("/delete_assessments/{assessment_id}")
def delete_assessment(assessment_id: int, db: Session = Depends(get_db)):
    return AssessmentService.delete_assessment(assessment_id=assessment_id, db=db)

