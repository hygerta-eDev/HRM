from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .employee_work_experienceService import WorkExperienceService
from Schema.work_experienceSchema import WorkExperienceCreate
from Config.database import get_db

router = APIRouter(prefix="/workExperience", tags=["WorkExperience"])

@router.get("/")
def get_all_workExperience(db: Session = Depends(get_db)):
    return WorkExperienceService.get_all_workExperience(db=db)

@router.post("/create_WorkExperience")
def create_workExperience(WorkExperiences: WorkExperienceCreate, db: Session = Depends(get_db)):
    return WorkExperienceService.create_workExperience(WorkExperiences, db)

