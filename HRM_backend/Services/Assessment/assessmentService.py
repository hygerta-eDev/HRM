from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.assessmentModel import Assessment
from Schema.assesmentSchema import AssessmentCreate,AssessmentUpdate


class AssessmentService:
    @staticmethod
    def get_all_assessments(db: Session = Depends(get_db)):
        return db.query(Assessment).all()
    @staticmethod
    def get_all_active_assessments(db: Session = Depends(get_db)):
        return db.query(Assessment).filter(Assessment.deleted_at == None).all()
    @staticmethod
    def get_assessment_by_id(db: Session, assessment_id: int):
        return db.query(Assessment).filter(Assessment.id == assessment_id).first()
    
    
    def create_assessment(Assessments: AssessmentCreate, db: Session = Depends(get_db)):

        db_assessment = Assessment(
            employee_id=Assessments.employee_id,
            user_id = Assessments.user_id,
            job_position_id = Assessments.job_position_id,
            evaluation_period = Assessments.evaluation_period,
            rate = Assessments.rate,
            finished = Assessments.finished,
            status = Assessments.status,
            performance_objectives = Assessments.performance_objectives,
            general_evaluation = Assessments.general_evaluation,
            employee_notes = Assessments.employee_notes,
            employee_notes_date=Assessments.employee_notes_date,
            created_at=Assessments.created_at
        )

        db.add(db_assessment)
        db.commit()
        db.refresh(db_assessment)

        return db_assessment
    @staticmethod
    def update_assessments(assessment_id: int, assessment: AssessmentUpdate, db: Session = Depends(get_db)):
        db_assessments = db.query(Assessment).filter(Assessment.deleted_at == None, Assessment.id == assessment_id).first()

        if db_assessments:
            if assessment.employee_id is not None:
                db_assessments.employee_id = assessment.employee_id
            if assessment.job_position_id is not None:
                db_assessments.job_position_id = assessment.job_position_id
            if assessment.user_id is not None:
                db_assessments.user_id = assessment.user_id
            if assessment.evaluation_period is not None:
                db_assessments.evaluation_period = assessment.evaluation_period
            if assessment.rate is not None:
                db_assessments.rate = assessment.rate
            if assessment.finished is not None:
                db_assessments.finished = assessment.finished
            if assessment.status is not None:
                db_assessments.status = assessment.status
            if assessment.performance_objectives is not None:
                db_assessments.performance_objectives = assessment.performance_objectives
            if assessment.employee_notes is not None:
                db_assessments.employee_notes = assessment.employee_notes
            if assessment.general_evaluation is not None:
                db_assessments.general_evaluation = assessment.general_evaluation
            if assessment.employee_notes_date is not None:
                db_assessments.employee_notes_date = assessment.employee_notes_date
            if assessment.updated_at is not None:
                db_assessments.updated_at = assessment.updated_at

            db.commit()
            db.refresh(db_assessments)

        return db_assessments

    
    @staticmethod
    def delete_assessment(assessment_id: int, db: Session):
        db_assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()

        if db_assessment:
            db_assessment.soft_delete()  
            db.commit()

        return db_assessment