from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.rolesModel import Roles
from Schema.rolesSchema import RolesCreate

class RolesService:
    @staticmethod
    def get_all_roles(db: Session = Depends(get_db)):
        return db.query(Roles).all()
    
    def create_roles(Role: RolesCreate, db: Session = Depends(get_db)):
 
        db_roles = Roles(
            name=Role.name,
            
        )

        db.add(db_roles)
        db.commit()
        db.refresh(db_roles)

        return db_roles

   