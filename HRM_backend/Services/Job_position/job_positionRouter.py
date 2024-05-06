from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .job_positionService import JobPositionService
from Schema.job_positionSchema import JobPositionCreate,JobPositionUpdate
from Config.database import get_db

router = APIRouter(prefix="/jobPosition", tags=["JobPosition"])

@router.get("/")
def get_all_jobPosition(db: Session = Depends(get_db)):
    return JobPositionService.get_all_jobPosition(db=db)

@router.get("/{jobPosition_id}")
def get_jobPosition(jobPosition_id: int, db: Session = Depends(get_db)):
    jobPosition = JobPositionService.get_jobPosition_by_id(db, jobPosition_id)
    if jobPosition is None:
        raise HTTPException(status_code=404, detail="jobPosition not found")
    return jobPosition

@router.post("/create_jobPosition")
def create_jobPosition(JobPosition: JobPositionCreate, db: Session = Depends(get_db)):
    return JobPositionService.create_jobPosition(JobPosition, db)

@router.put("/update_jobPosition/{jobPosition_id}")
def update_jobPosition(jobPosition_id: int, jobPosition: JobPositionUpdate, db: Session = Depends(get_db)):
    return JobPositionService.update_jobPosition(jobPosition_id=jobPosition_id, jobPosition=jobPosition, db=db)

@router.delete("/delete_jobPosition/{jobPosition_id}")
def delete_jobPosition(jobPosition_id: int, db: Session = Depends(get_db)):
    return JobPositionService.delete_jobPosition(jobPosition_id=jobPosition_id, db=db)
