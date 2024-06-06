from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .rolesService import RolesService
from Schema.rolesSchema import RolesCreate
from Config.database import get_db

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/")
def get_all_roles(db: Session = Depends(get_db)):
    return RolesService.get_all_roles(db=db)

@router.post("/create_roles")
def create_roles(LeaveTypes: RolesCreate, db: Session = Depends(get_db)):
    return RolesService.create_roles(LeaveTypes, db)

