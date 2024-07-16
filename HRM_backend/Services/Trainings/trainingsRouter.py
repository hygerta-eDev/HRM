from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .trainingsService import TrainingService
from Schema.trainingSchema import TrainingCreate,EmployeeTrainingCreate,TrainingUpdate, EmployeeTrainingUpdate,AssignEmployeeTraining
from Config.database import get_db
from typing import List
router = APIRouter(prefix="/training", tags=["Training"])

@router.get("/")
def get_all_training(db: Session = Depends(get_db)):
    return TrainingService.get_all_training(db=db)

@router.get("/active_trainings")
def get_all_active_trainings(db: Session = Depends(get_db)):
    return TrainingService.get_all_active_trainings(db=db)

@router.get("/{training_id}")
def get_training(training_id: int, db: Session = Depends(get_db)):
    training = TrainingService.get_training_by_id(db, training_id)
    if training is None:
        raise HTTPException(status_code=404, detail="training not found")
    return training

@router.post("/create_training")
def create_training(Training: TrainingCreate, db: Session = Depends(get_db)):
    return TrainingService.create_training(Training, db)

@router.put("/update_trainings/{training_id}")
def update_trainings(training_id: int, training: TrainingUpdate, db: Session = Depends(get_db)):
    training=TrainingService.update_trainings(training_id=training_id, training=training, db=db)
    if training is None:
        raise HTTPException(status_code=404, detail="training not found or has been soft-deleted")
    return training

@router.delete("/delete_training/{training_id}")
def delete_training(training_id: int, db: Session = Depends(get_db)):
    return TrainingService.delete_training(training_id=training_id, db=db)


''' Employee training'''

@router.get("/employee_training/all_employee_training")
def get_all_employeeTraining(db: Session = Depends(get_db)):
    return TrainingService.get_all_employeeTraining(db=db)

@router.post("/create_employee_training")
def create_get_all_employeeTraining(Training: EmployeeTrainingCreate, db: Session = Depends(get_db)):
    return TrainingService.create_get_all_employeeTraining(Training, db)

@router.put("/update_employee_training/{employeeTraining_id}")
def update_employeeTraining(employeeTraining_id: int, employeeTraining: EmployeeTrainingUpdate, db: Session = Depends(get_db)):
    institution=TrainingService.update_employeeTraining(employeeTraining_id=employeeTraining_id, employeeTraining=employeeTraining, db=db)
    if institution is None:
        raise HTTPException(status_code=404, detail="Institution not found or has been soft-deleted")
    return institution

@router.delete("/delete_employeeTraining/{employeeTraining_id}")
def delete_employeeTraining(employeeTraining_id: int, db: Session = Depends(get_db)):
    return TrainingService.delete_employeeTraining(employeeTraining_id=employeeTraining_id, db=db)

@router.get("/{training_id}/assigned_employees", response_model=List[AssignEmployeeTraining])
def get_assigned_employees(training_id: int, db: Session = Depends(get_db)):
    return TrainingService.get_assigned_employees(training_id, db)