from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .work_termination_reasonService import TerminationReasonService
from Schema.work_termination_reasonSchema import TerminationReasonCreate
from Config.database import get_db

router = APIRouter(prefix="/terminationReason", tags=["TerminationReason"])

@router.get("/")
def get_all_terminationReason(db: Session = Depends(get_db)):
    return TerminationReasonService.get_all_terminationReason(db=db)

@router.post("/create_terminationReason")
def create_terminationReason(TerminationReasons: TerminationReasonCreate, db: Session = Depends(get_db)):
    return TerminationReasonService.create_terminationReason(TerminationReasons, db)

