from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .job_positionService import JobPositionService
from Schema.job_positionSchema import JobPositionCreate
from Config.database import get_db

router = APIRouter(prefix="/jobPosition", tags=["JobPosition"])

@router.get("/")
def get_all_jobPosition(db: Session = Depends(get_db)):
    return JobPositionService.get_all_jobPosition(db=db)

@router.post("/create_jobPosition")
def create_jobPosition(JobPosition: JobPositionCreate, db: Session = Depends(get_db)):
    return JobPositionService.create_jobPosition(JobPosition, db)

