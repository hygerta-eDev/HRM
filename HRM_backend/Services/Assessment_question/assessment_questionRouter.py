from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .assessment_questionService import AssessmentQuestionService
from Schema.assessment_questionSchema import AssessmentQuestionCreate
from Config.database import get_db

router = APIRouter(prefix="/assessment_question", tags=["Assessment_question"])

@router.get("/")
def get_all_assessmentQuestion(db: Session = Depends(get_db)):
    return AssessmentQuestionService.get_all_assessmentQuestion(db=db)

@router.post("/create_assessmentQuestion")
def create_assessmentQuestion(AssessmentsQuestions: AssessmentQuestionCreate, db: Session = Depends(get_db)):
    return AssessmentQuestionService.create_assessmentQuestion(AssessmentsQuestions, db)


