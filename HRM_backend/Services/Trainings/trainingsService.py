from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.trainingsModel import Training
from Models.employeeTrainingModel import EmployeeTraining
from Schema.trainingSchema import TrainingCreate,EmployeeTrainingCreate


class TrainingService:
    @staticmethod
    def get_all_training(db: Session = Depends(get_db)):
        return db.query(Training).all()
    
    def create_training(Trainings: TrainingCreate, db: Session = Depends(get_db)):

        db_assessment = Training(
            title=Trainings.title,
            start_date = Trainings.start_date,
            end_date = Trainings.end_date,
            description = Trainings.description,
            outcome = Trainings.outcome,
            user_id = Trainings.user_id,
            active = Trainings.active,
            completed_at = Trainings.completed_at,
            created_at = Trainings.created_at,
            updated_at=Trainings.updated_at,
            deleted_at = Trainings.deleted_at

        )

        db.add(db_assessment)
        db.commit()
        db.refresh(db_assessment)

        return db_assessment
    
    def get_all_employeeTraining(db: Session = Depends(get_db)):
        return db.query(EmployeeTraining).all()
    
    def create_get_all_employeeTraining(EmployeeTrainings: EmployeeTrainingCreate, db: Session = Depends(get_db)):

        db_employeeTraining = EmployeeTraining(
            employee_id=EmployeeTrainings.employee_id,
            training_id = EmployeeTrainings.training_id,

        )

        db.add(db_employeeTraining)
        db.commit()
        db.refresh(db_employeeTraining)

        return db_employeeTraining