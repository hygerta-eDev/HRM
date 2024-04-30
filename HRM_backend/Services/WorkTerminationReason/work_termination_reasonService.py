from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.workTerminationReasonModel import TerminationReason
from Schema.work_termination_reasonSchema import TerminationReasonCreate


class TerminationReasonService:
    @staticmethod
    def get_all_terminationReason(db: Session = Depends(get_db)):
        return db.query(TerminationReason).all()
    
    def create_terminationReason(TerminationReasons: TerminationReasonCreate, db: Session = Depends(get_db)):

        db_terminationReason = TerminationReason(
            name=TerminationReasons.name,
            slug=TerminationReasons.slug,
            created_at=TerminationReasons.created_at,
            updated_at=TerminationReasons.updated_at,
            deleted_at =TerminationReasons.deleted_at
        )

        db.add(db_terminationReason)
        db.commit()
        db.refresh(db_terminationReason)

        return db_terminationReason
