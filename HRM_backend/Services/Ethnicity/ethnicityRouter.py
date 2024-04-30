from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .ethnicityService import EthnicityService
from Schema.ethnicitySchema import EthnicityCreate
from Config.database import get_db

router = APIRouter(prefix="/ethnicity", tags=["Ethnicity"])

@router.get("/")
def get_all_ethnicities(db: Session = Depends(get_db)):
    return EthnicityService.get_all_ethnicities(db=db)

@router.post("/create_ethnicity")
def create_ethnicity(Ethnicity: EthnicityCreate, db: Session = Depends(get_db)):
    return EthnicityService.create_ethnicity(Ethnicity, db)

