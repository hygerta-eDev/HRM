from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.assessmentQuestionsModel import AssessmentQuestion
from Schema.assessment_questionSchema import AssessmentQuestionCreate,AssessmentQuestionUpdate


class AssessmentQuestionService:
    @staticmethod
    def get_all_assessmentQuestion(db: Session = Depends(get_db)):
        return db.query(AssessmentQuestion).all()
    @staticmethod
    def get_all_active_assessmentQuestions(db: Session = Depends(get_db)):
        return db.query(AssessmentQuestion).filter(AssessmentQuestion.deleted_at == None).all()
    @staticmethod
    def get_assessmentQuestion_by_id(db: Session, assessmentQuestion_id: int):
        return db.query(AssessmentQuestion).filter(AssessmentQuestion.id == assessmentQuestion_id).first()
    
    def create_assessmentQuestion(assessment_questions: AssessmentQuestionCreate, db: Session = Depends(get_db)):

            db_assessment = AssessmentQuestion(
                title=assessment_questions.title,
                description=assessment_questions.description,
                options=assessment_questions.options,
                weight=assessment_questions.weight,
                selected_option=assessment_questions.selected_option,
                notes=assessment_questions.notes,
                assessment_id=assessment_questions.assessment_id,
                user_id=assessment_questions.user_id,
                created_at=assessment_questions.created_at,
            )

            db.add(db_assessment)
            db.commit()
            db.refresh(db_assessment)

            return db_assessment
    @staticmethod
    def update_assessment_questions(assessmentQuestion_id: int, assessment_questions: AssessmentQuestionUpdate, db: Session = Depends(get_db)):
        db_assessmentQuestions = db.query(AssessmentQuestion).filter(AssessmentQuestion.deleted_at == None, AssessmentQuestion.id == assessmentQuestion_id).first()

        if db_assessmentQuestions:
            if assessment_questions.title is not None:
                db_assessmentQuestions.title = assessment_questions.title
            if assessment_questions.description is not None:
                db_assessmentQuestions.description = assessment_questions.description
            if assessment_questions.options is not None:
                db_assessmentQuestions.options = assessment_questions.options
            if assessment_questions.weight is not None:
                db_assessmentQuestions.weight = assessment_questions.weight
            if assessment_questions.selected_option is not None:
                db_assessmentQuestions.selected_option = assessment_questions.selected_option
            if assessment_questions.notes is not None:
                db_assessmentQuestions.notes = assessment_questions.notes
            if assessment_questions.user_id is not None:
                db_assessmentQuestions.user_id = assessment_questions.user_id
            if assessment_questions.updated_at is not None:
                db_assessmentQuestions.updated_at = assessment_questions.updated_at
            db.commit()
            db.refresh(db_assessmentQuestions)

        return db_assessmentQuestions

    
    @staticmethod
    def delete_assessmentQuestions(assessmentQuestion_id: int, db: Session):
        db_assessmentQuestion = db.query(AssessmentQuestion).filter(AssessmentQuestion.id == assessmentQuestion_id).first()

        if db_assessmentQuestion:
            db_assessmentQuestion.soft_delete()  
            db.commit()

        return db_assessmentQuestion
    