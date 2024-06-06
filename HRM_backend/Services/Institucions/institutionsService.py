from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Config.database import get_db
from Models.institutionModel import Institution
from Models.ethnicitiesModel import Ethnicities
from Models.departmentsModel import Departments
from Models.jobPositionModel import JobPosition
from Models.registersModel import Log
from Schema.institutionsSchema import InstitutionCreate, InstitutionUpdate,InstitutionResponse
from Config.logging_utils import log_function_call
from typing import Any, Optional
from sqlalchemy import func

class InstitutionService:

    @staticmethod
    @log_function_call(entity_name="Institution")
    def get_all_institutions(db: Session = Depends(get_db)):
        return db.query(Institution).all()
    
    @staticmethod
    @log_function_call(entity_name="Institution")
    def get_all_active_institutions(db: Session = Depends(get_db)):
        return db.query(Institution).filter(Institution.deleted_at == None).all()
    
    @staticmethod
    @log_function_call(entity_name="Institution")
    def get_institution_by_id(db: Session, entity_id: int) -> Optional[Institution]:
        return db.query(Institution).filter(Institution.id == entity_id).first()
    
    @staticmethod
    @log_function_call(entity_name="Institution")
    def create_institutions(InstitutionData: InstitutionCreate, db: Session ) -> InstitutionResponse:
        db_institution = Institution(
            name=InstitutionData.name,
            slug=InstitutionData.slug,
            user_id=InstitutionData.user_id,
            active=InstitutionData.active,
            # created_at=InstitutionData.created_at
        )
        db.add(db_institution)
        db_institution.created_at = func.now()
        db.commit()
        db.refresh(db_institution)
        
        return db_institution
    
    # @staticmethod
    # @log_function_call
    # def create_institutions(entity_data: Any, entity_type: Any, db: Session = Depends(get_db), user_id: int = 1):
    #     db_entity = entity_type(**entity_data.dict())
    #     db.add(db_entity)
    #     db.commit()
    #     db.refresh(db_entity)
    #     return db_entity

    # @log_function_call
    # @staticmethod
    # def update_institutions(institution_id: int, institucion: InstitutionUpdate, db: Session = Depends(get_db))-> InstitutionResponse:
    #     db_institutions = db.query(Institution).filter(Institution.deleted_at == None, Institution.id == institution_id).first()

    #     if db_institutions:
    #         if institucion.name is not None:
    #             db_institutions.name = institucion.name
    #         if institucion.slug is not None:
    #             db_institutions.slug = institucion.slug
    #         if institucion.user_id is not None:
    #             db_institutions.user_id = institucion.user_id
    #         if institucion.active is not None:
    #             db_institutions.active = institucion.active
    #         if institucion.updated_at is not None:
    #             db_institutions.updated_at = institucion.updated_at
    #         db.commit()
    #         db.refresh(db_institutions)

    #     return db_institutions

    @staticmethod
    @log_function_call(entity_name="Institution")
    def update_institution(institution_id: int, institution_data: 'InstitutionUpdate', entity_id: int, entity_type: Any, db: Session = Depends(get_db), user_id: int = 1, **kwargs):
        db_institution = db.query(Institution).filter(Institution.deleted_at == None, Institution.id == institution_id).first()

        if not db_institution:
            raise HTTPException(status_code=404, detail="Institution not found")

        changes = {}
        for field, value in institution_data.dict(exclude_unset=True).items():
            if getattr(db_institution, field) != value:
                changes[field] = (getattr(db_institution, field), value)
                setattr(db_institution, field, value)

        kwargs['changes'] = changes  # Pass changes to kwargs for logging

        if changes:
            db_institution.updated_at = func.now()
            db.commit()
            db.refresh(db_institution)

        return db_institution
    
    @staticmethod
    @log_function_call(entity_name="Institution")
    def delete_institution(entity_id: int, db: Session):
        db_institution = db.query(Institution).filter(Institution.id == entity_id).first()

        if db_institution:
            db_institution.soft_delete()  
            db.commit()

        return db_institution
    
    # @staticmethod
    # def get_department_job_positions(department_id: int, db: Session = Depends(get_db)):
    #     department = db.query(Departments).filter(Departments.id == department_id).first()
    #     if department is None:
    #         raise HTTPException(status_code=404, detail="Department not found")
    #     job_positions = department.job_positions
    #     return {"department_id": department_id, "job_positions": job_positions}


    # def get_job_positions_for_department(db: Session, institution_id: int, department_id: int):
    #     return db.query(JobPosition).\
    #         join(Departments, JobPosition.department_id == Departments.id).\
    #         filter(Departments.institution_id == institution_id).\
    #         filter(Departments.id == department_id).\
    #         all()
    # job_positions = get_job_positions_for_department(get_db, institution_id=1, department_id=2)
    # print(job_positions)