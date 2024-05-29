from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .job_positionService import JobPositionService
from Schema.job_positionSchema import JobPositionCreate,JobPositionUpdate,JobPositionSchema
from Config.database import get_db
from typing import List



router = APIRouter(prefix="/jobPosition", tags=["JobPosition"])

@router.get("/")
def get_all_jobPosition(db: Session = Depends(get_db)):
    return JobPositionService.get_all_jobPosition(db=db)

@router.get("/active_jobPosition",response_model=List[JobPositionSchema])
def get_all_active_jobPosition(db: Session = Depends(get_db),):
    return JobPositionService.get_all_active_jobPosition(db=db)

@router.get("/{jobPosition_id}", response_model=JobPositionSchema)
def get_jobPosition(jobPosition_id: int, db: Session = Depends(get_db)):
    jobPosition = JobPositionService.get_jobPosition_by_id(db, entity_id=jobPosition_id)
    if jobPosition is None:
        raise HTTPException(status_code=404, detail="jobPosition not found")
    return jobPosition

@router.post("/create_jobPosition", response_model=JobPositionCreate)
def create_jobPosition(JobPosition: JobPositionCreate, db: Session = Depends(get_db)):
    return JobPositionService.create_jobPosition(JobPosition, db)

@router.put("/update_jobPosition/{jobPosition_id}")
async def update_jobPosition(jobPosition_id: int, jobPosition: JobPositionUpdate, db: Session = Depends(get_db)):
    updated_job_position = JobPositionService.update_jobPosition(jobPosition_id, jobPosition, db)
    if updated_job_position:
        return updated_job_position
    else:
        raise HTTPException(status_code=404, detail="JobPosition not found")
@router.delete("/delete_jobPosition/{jobPosition_id}")
def delete_jobPosition(jobPosition_id: int, db: Session = Depends(get_db)):
    return JobPositionService.delete_jobPosition(entity_id=jobPosition_id, db=db)
