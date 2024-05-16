from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .ethnicityService import EthnicityService
from Schema.ethnicitySchema import EthnicityCreate
from Config.database import get_db

router = APIRouter(prefix="/ethnicities", tags=["Ethnicity"])

@router.get("/")
def get_all_ethnicities(db: Session = Depends(get_db)):
    return EthnicityService.get_all_ethnicities(db=db)

@router.get("/active_ethnicities")
def get_all_active_ethnicities(db: Session = Depends(get_db)):
    return EthnicityService.get_all_active_ethnicities(db=db)

@router.get("/{ethnicity_id}")
def get_ethnicity(ethnicity_id: int, db: Session = Depends(get_db)):
    ethnicity = EthnicityService.get_ethnicities_by_id(db, ethnicity_id)
    if ethnicity is None:
        raise HTTPException(status_code=404, detail="ethnicity not found")
    return ethnicity

@router.post("/create_ethnicity")
def create_ethnicity(Ethnicity: EthnicityCreate, db: Session = Depends(get_db)):
    return EthnicityService.create_ethnicity(Ethnicity, db)


@router.put("/update_ethnicity/{ethnicity_id}")
def update_ethnicity(ethnicity_id: int, ethnicity: EthnicityCreate, db: Session = Depends(get_db)):
    ethnicity=EthnicityService.update_ethnicity(ethnicity_id=ethnicity_id, ethnicity=ethnicity, db=db)
    if ethnicity is None:
        raise HTTPException(status_code=404, detail="ethnicity not found or has been soft-deleted")
    return ethnicity

@router.delete("/delete_ethnicity/{ethnicity_id}")
def delete_ethnicity(ethnicity_id: int, db: Session = Depends(get_db)):
    return EthnicityService.delete_ethnicity(ethnicity_id=ethnicity_id, db=db)
