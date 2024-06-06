from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .assessment_questionService import AssessmentQuestionService
from Schema.assessment_questionSchema import AssessmentQuestionCreate,AssessmentQuestionUpdate
from Config.database import get_db

router = APIRouter(prefix="/assessment_question", tags=["Assessment_question"])

@router.get("/")
def get_all_assessmentQuestion(db: Session = Depends(get_db)):
    return AssessmentQuestionService.get_all_assessmentQuestion(db=db)


@router.get("/active_assessmentQuestions")
def get_all_active_assessmentQuestions(db: Session = Depends(get_db)):
    return AssessmentQuestionService.get_all_active_assessmentQuestions(db=db)

@router.get("/{assessmentQuestion_id}")
def get_assessmentQuestion_by_id(assessmentQuestion_id: int, db: Session = Depends(get_db)):
    assessment_questions = AssessmentQuestionService.get_assessmentQuestion_by_id(db, assessmentQuestion_id)
    if assessment_questions is None:
        raise HTTPException(status_code=404, detail="assessment_questions not found")
    return assessment_questions

@router.post("/create_assessmentQuestion")
def create_assessmentQuestion(AssessmentsQuestions: AssessmentQuestionCreate, db: Session = Depends(get_db)):
    return AssessmentQuestionService.create_assessmentQuestion(AssessmentsQuestions, db)


@router.put("/update_assessment_questionss/{assessmentQuestion_id}")
def update_assessment_questionss(assessmentQuestion_id: int, assessment_questions: AssessmentQuestionUpdate, db: Session = Depends(get_db)):
    assessment_question=AssessmentQuestionService.update_assessment_questions(assessmentQuestion_id=assessmentQuestion_id, assessment_questions=assessment_questions, db=db)
    if assessment_question is None:
        raise HTTPException(status_code=404, detail="assessment_questions not found or has been soft-deleted")
    return assessment_question

@router.delete("/delete_assessmentQuestions/{assessmentQuestion_id}")
def delete_assessmentQuestions(assessmentQuestion_id: int, db: Session = Depends(get_db)):
    return AssessmentQuestionService.delete_assessmentQuestions(assessmentQuestion_id=assessmentQuestion_id, db=db)


