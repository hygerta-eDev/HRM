from fastapi import APIRouter, Depends, HTTPException, Form, HTTPException, Path, Body
from sqlalchemy.orm import Session
from .assessmentService import AssessmentService
from Schema.assesmentSchema import AssessmentCreate,AssessmentUpdate
from Config.database import get_db
from pydantic import BaseModel
from Models.assessmentQuestionsModel import AssessmentQuestion
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


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

class UpdateQuestionOption(BaseModel):
    selected_option: str

# @router.put("/update_assessment_question_option/{question_id}")
# def update_assessment_question_option(question_id: int, update_data: UpdateQuestionOption, db: Session = Depends(get_db)):
#     question = db.query(AssessmentQuestion).filter(AssessmentQuestion.id == question_id).first()
    
#     if not question:
#         raise HTTPException(status_code=404, detail="Question not found")
    
#     question.selected_option = update_data.selected_option
#     db.commit()
#     db.refresh(question)
    
#     logging.info(f"Updated Question with ID: {question.id}, selected_option: {question.selected_option}")
#     return {"message": "Question updated successfully"}


@router.put("/update_assessment_question_option/{question_id}")
def update_assessment_question_option(question_id: int, update_data: dict, db: Session = Depends(get_db)):
    question = db.query(AssessmentQuestion).filter(AssessmentQuestion.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    selected_option = update_data.get('selected_option')
    if selected_option is not None:
        question.selected_option = selected_option

    # Update the weight based on selected_option
    weight = AssessmentService.process_question_update(question_id, selected_option, db)
    question.weight = weight  # Ensure weight is updated in the question object

    db.commit()
    db.refresh(question)
    
    return {
        "message": "Question updated successfully",
        "question": {
            "id": question.id,
            "selected_option": question.selected_option,
            "weight": question.weight
        }
    }

    
