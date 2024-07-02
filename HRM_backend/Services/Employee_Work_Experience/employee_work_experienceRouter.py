from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .employee_work_experienceService import WorkExperienceService
from Schema.work_experienceSchema import WorkExperienceCreate, WorkExperienceUpdate,WorkExperienceCreates,WorkExperienceTest
from Config.database import get_db
from typing import List 
from Schema.enums.work_experience import Work_experience
from Models.employeeWorkExperienceModel import WorkExperience

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
@router.post("/create_WorkExperience", response_model=List[WorkExperienceCreates])
def create_workExperience(WorkExperiences: List[WorkExperienceCreate], db: Session = Depends(get_db)):
    return WorkExperienceService.create_work_experience(WorkExperiences, db)

@router.put("/update_workExperiences/{workExperience_id}")
def update_workExperiences(workExperience_id: int, workExperience: WorkExperienceUpdate, db: Session = Depends(get_db)):
    workExperience=WorkExperienceService.update_workExperiences(workExperience_id=workExperience_id, workExperience=workExperience, db=db)
    if workExperience is None:
        raise HTTPException(status_code=404, detail="workExperience not found or has been soft-deleted")
    return workExperience

@router.delete("/delete_workExperience/{workExperience_id}")
def delete_workExperience(workExperience_id: int, db: Session = Depends(get_db)):
    return WorkExperienceService.delete_workExperience(workExperience_id=workExperience_id, db=db)

@router.get("/work_experience/type")
def get_work_experience_type():
    work_experience_type = [status.value for status in Work_experience]
    return work_experience_type

@router.get("/employees/{employee_id}/work_experiences", response_model=List[WorkExperienceTest])
def get_work_experiences(employee_id: int, db: Session = Depends(get_db)):
    work_experiences = db.query(WorkExperience).filter(WorkExperience.employee_id == employee_id).all()
    if not work_experiences:
        raise HTTPException(status_code=404, detail="Work experiences not found")
    return work_experiences


@router.put("/employees/{employee_id}/work_experiences", response_model=List[WorkExperienceTest])
def update_work_experiences(
    employee_id: int,
    workExperience: List[WorkExperienceTest],
    db: Session = Depends(get_db)
):
    updated_experiences = []
    for experience in workExperience:
        updated_experience = WorkExperienceService.update_workExperiences_employee(
            employee_id=employee_id,
            workExperience=experience,
            db=db
        )
        if updated_experience:
            updated_experiences.append(updated_experience)
        else:
            raise HTTPException(status_code=404, detail=f"Work Experience not found for ID {experience.id}")

    return updated_experiences