from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .employee_work_experienceService import WorkExperienceService
from Schema.work_experienceSchema import WorkExperienceCreate, WorkExperienceUpdate
from Config.database import get_db

router = APIRouter(prefix="/workExperience", tags=["WorkExperience"])

@router.get("/")
def get_all_workExperience(db: Session = Depends(get_db)):
    return WorkExperienceService.get_all_workExperience(db=db)

@router.get("/WorkExperiences")
def get_all_active_workExperiences(db: Session = Depends(get_db)):
    return WorkExperienceService.get_all_active_workExperiences(db=db)

@router.get("/{workExperience_id}")
def get_workExperience(workExperience_id: int, db: Session = Depends(get_db)):
    workExperience = WorkExperienceService.get_workExperience_by_id(db, workExperience_id)
    if workExperience is None:
        raise HTTPException(status_code=404, detail="workExperience not found")
    return workExperience

@router.post("/create_WorkExperience")
def create_workExperience(WorkExperiences: WorkExperienceCreate, db: Session = Depends(get_db)):
    return WorkExperienceService.create_workExperience(WorkExperiences, db)

@router.put("/update_workExperiences/{workExperience_id}")
def update_workExperiences(workExperience_id: int, workExperience: WorkExperienceUpdate, db: Session = Depends(get_db)):
    workExperience=WorkExperienceService.update_workExperiences(workExperience_id=workExperience_id, workExperience=workExperience, db=db)
    if workExperience is None:
        raise HTTPException(status_code=404, detail="workExperience not found or has been soft-deleted")
    return workExperience

@router.delete("/delete_workExperience/{workExperience_id}")
def delete_workExperience(workExperience_id: int, db: Session = Depends(get_db)):
    return WorkExperienceService.delete_workExperience(workExperience_id=workExperience_id, db=db)

