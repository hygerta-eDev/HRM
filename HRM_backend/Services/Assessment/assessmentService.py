from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.assessmentModel import Assessment
from Schema.assesmentSchema import AssessmentCreate


class AssessmentService:
    @staticmethod
    def get_all_assessmentQuestion(db: Session = Depends(get_db)):
        return db.query(Assessment).all()
    
    def create_assessmentQuestion(Assessments: AssessmentCreate, db: Session = Depends(get_db)):

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
            created_at = Assessments.created_at,
            updated_at=Assessments.updated_at,
            deleted_at = Assessments.deleted_at

        )

        db.add(db_assessment)
        db.commit()
        db.refresh(db_assessment)

        return db_assessment
