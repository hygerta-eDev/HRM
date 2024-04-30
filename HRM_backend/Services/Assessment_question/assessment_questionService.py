from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.assessmentQuestionsModel import AssessmentQuestion
from Schema.assessment_questionSchema import AssessmentQuestionCreate


class AssessmentQuestionService:
    @staticmethod
    def get_all_assessmentQuestion(db: Session = Depends(get_db)):
        return db.query(AssessmentQuestion).all()
    
    def create_assessmentQuestion(assessment_questions: AssessmentQuestionCreate, db: Session = Depends(get_db)):

            db_assessment = AssessmentQuestion(
                title=assessment_questions.title,
                description=assessment_questions.description,
                options=assessment_questions.options,
                weight=assessment_questions.weight,
                selected_option=assessment_questions.selected_option,
                notes=assessment_questions.notes,
                assessment_id=assessment_questions.assessment_id,
                # employee_notes=assessment_questions.employee_notes,
                # created_at=assessment_questions.created_at,
                # updated_at=assessment_questions.updated_at,
                # deleted_at=assessment_questions.deleted_at

            )

            db.add(db_assessment)
            db.commit()
            db.refresh(db_assessment)

            return db_assessment