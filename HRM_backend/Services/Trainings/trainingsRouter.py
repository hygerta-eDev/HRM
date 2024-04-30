from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .trainingsService import TrainingService
from Schema.trainingSchema import TrainingCreate,EmployeeTrainingCreate
from Config.database import get_db

router = APIRouter(prefix="/training", tags=["Training"])

@router.get("/")
def get_all_training(db: Session = Depends(get_db)):
    return TrainingService.get_all_training(db=db)

@router.post("/create_training")
def create_training(Training: TrainingCreate, db: Session = Depends(get_db)):
    return TrainingService.create_training(Training, db)
@router.get("/employee_training")
def get_all_employeeTraining(db: Session = Depends(get_db)):
    return TrainingService.get_all_employeeTraining(db=db)

@router.post("/create_employee_training")
def create_get_all_employeeTraining(Training: EmployeeTrainingCreate, db: Session = Depends(get_db)):
    return TrainingService.create_get_all_employeeTraining(Training, db)


