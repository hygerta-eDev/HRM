from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.trainingsModel import Training
from Models.employeeTrainingModel import EmployeeTraining
from Models.employeeModel import Employees
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

from Schema.trainingSchema import TrainingCreate,EmployeeTrainingCreate,TrainingUpdate,EmployeeTrainingUpdate,AssignEmployeeTraining


class TrainingService:
    @staticmethod
    def get_all_training(db: Session = Depends(get_db)):
        return db.query(Training).all()
    @staticmethod
    def get_all_active_trainings(db: Session = Depends(get_db)):
        return db.query(Training).filter(Training.deleted_at == None).all()
    @staticmethod
    def get_training_by_id(db: Session, training_id: int):
        return db.query(Training).filter(Training.id == training_id).first()
    
    # def create_training(Trainings: TrainingCreate, db: Session = Depends(get_db)):

    #     db_assessment = Training(
    #         title=Trainings.title,
    #         start_date = Trainings.start_date,
    #         end_date = Trainings.end_date,
    #         description = Trainings.description,
    #         outcome = Trainings.outcome,
    #         user_id = Trainings.user_id,
    #         active = Trainings.active,
    #         completed_at = Trainings.completed_at,
    #         created_at = Trainings.created_at,
    #     )

    #     db.add(db_assessment)
    #     db.commit()
    #     db.refresh(db_assessment)

    #     return db_assessment
    def create_training(Trainings: TrainingCreate, db: Session = Depends(get_db)):
        # Determine active status based on completed_at field
        is_active = not bool(Trainings.completed_at)

        db_assessment = Training(
            title=Trainings.title,
            start_date=Trainings.start_date,
            end_date=Trainings.end_date,
            description=Trainings.description,
            # outcome=Trainings.outcome,
            user_id=Trainings.user_id,
            active=is_active,  # Use the determined active status
            completed_at=Trainings.completed_at,
            created_at=Trainings.created_at,
        )

        db.add(db_assessment)
        db.commit()
        db.refresh(db_assessment)

        return db_assessment
    @staticmethod
    def update_trainings(training_id: int, training: TrainingUpdate, db: Session = Depends(get_db)):
        db_trainings = db.query(Training).filter(Training.deleted_at == None, Training.id == training_id).first()

        if db_trainings:
            if training.title is not None:
                db_trainings.title = training.title
            if training.start_date is not None:
                db_trainings.start_date = training.start_date
            if training.user_id is not None:
                db_trainings.user_id = training.user_id
            if training.description is not None:
                db_trainings.description = training.description
            if training.outcome is not None:
                db_trainings.outcome = training.outcome
            if training.active is not None:
                db_trainings.active = training.active
            if training.completed_at is not None:
                db_trainings.completed_at = training.completed_at
            if training.updated_at is not None:
                db_trainings.updated_at = training.updated_at
            db.commit()
            db.refresh(db_trainings)

        return db_trainings

    
    @staticmethod
    def delete_training(training_id: int, db: Session):
        db_trainings = db.query(Training).filter(Training.id == training_id).first()

        if db_trainings:
            db_trainings.soft_delete()  
            db.commit()

        return db_trainings 

    '''Employee tainings'''

    def get_all_employeeTraining(db: Session = Depends(get_db)):
        return db.query(EmployeeTraining).all()
    
    def create_get_all_employeeTraining(EmployeeTrainings: EmployeeTrainingCreate, db: Session = Depends(get_db)):
        try:

            db_employeeTraining = EmployeeTraining(
                employee_id=EmployeeTrainings.employee_id,
                training_id = EmployeeTrainings.training_id,
                user_id = EmployeeTrainings.user_id,
                created_at=EmployeeTrainings.created_at
            )

            db.add(db_employeeTraining)
            db.commit()
            db.refresh(db_employeeTraining)

            return db_employeeTraining
        except IntegrityError as e:
                db.rollback()
                raise HTTPException(status_code=400, detail="Employee is already assigned to this training")
    
    @staticmethod
    def update_employeeTraining(employeeTraining_id: int, employeeTraining: EmployeeTrainingUpdate, db: Session = Depends(get_db)):
        db_employeeTraining = db.query(EmployeeTraining).filter(EmployeeTraining.deleted_at == None, EmployeeTraining.employee_id == employeeTraining_id).first()

        if db_employeeTraining:
            if employeeTraining.employee_id is not None:
                db_employeeTraining.employee_id = employeeTraining.employee_id
            if employeeTraining.training_id is not None:
                db_employeeTraining.training_id = employeeTraining.training_id
            if employeeTraining.user_id is not None:
                db_employeeTraining.user_id = employeeTraining.user_id
            if employeeTraining.updated_at is not None:
                db_employeeTraining.updated_at = employeeTraining.updated_at
            db.commit()
            db.refresh(db_employeeTraining)

        return db_employeeTraining

    
    @staticmethod
    def delete_employeeTraining(employeeTraining_id: int, db: Session):
        db_employeeTraining = db.query(EmployeeTraining).filter(EmployeeTraining.employee_id == employeeTraining_id).first()

        if db_employeeTraining:
            db_employeeTraining.soft_delete()  
            db.commit()

        return db_employeeTraining
    # @staticmethod
    # def get_assigned_employees(training_id: int, db: Session = Depends(get_db)):
    #     employees= db.query(EmployeeTraining).filter(EmployeeTraining.training_id == training_id).all()
    #     for employee in employees:
    #         employees_name = db.query(Employees.name).filter(Employees.id == employee.employee_id).scalar()
    #         employees_last_name = db.query(Employees.last_name).filter(Employees.id == employee.employee_id).scalar()

    #         employee.employee_id = employees_name
    #         employee.employee_last_name = employees_last_name

    #     return employees
    @staticmethod
    def delete_employee_from_training(training_id: int, employee_id: int, db: Session):
        # Query the EmployeeTraining entry to be deleted
        db_employeeTraining = db.query(EmployeeTraining).filter(
            EmployeeTraining.training_id == training_id,
            EmployeeTraining.employee_id == employee_id
        ).first()

        # If the entry exists, delete it
        if db_employeeTraining:
            db.delete(db_employeeTraining)
            db.commit()

        return db_employeeTraining
    @staticmethod
    def get_assigned_employees(training_id: int, db: Session = Depends(get_db)):
        employee_trainings = db.query(EmployeeTraining).filter(EmployeeTraining.training_id == training_id).options(joinedload(EmployeeTraining.employee)).all()

        assigned_employees = []
        for employee_training in employee_trainings:
            employee = db.query(Employees).filter(Employees.id == employee_training.employee_id).first()
            if employee:
                assigned_employees.append({
                    "employee_id": employee.id,
                    "name": employee.name,
                    "last_name": employee.last_name,
                    "training_id": employee_training.training_id,
                    "created_at": employee_training.created_at,
                    "user_id": employee_training.user_id,
                })

        return assigned_employees
