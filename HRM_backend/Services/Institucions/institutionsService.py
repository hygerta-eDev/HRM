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
from Schema.institutionsSchema import InstitutionCreate, InstitutionUpdate


class InstitutionService:
    @staticmethod
    def get_all_institutions(db: Session = Depends(get_db)):
        return db.query(Institution).all()
    
    @staticmethod
    def get_all_active_institutions(db: Session = Depends(get_db)):
        return db.query(Institution).filter(Institution.deleted_at == None).all()
    
    @staticmethod
    def get_institution_by_id(db: Session, institution_id: int):
        return db.query(Institution).filter(Institution.id == institution_id).first()
    
    def create_institutions(Institutions: InstitutionCreate, db: Session = Depends(get_db)):

        db_institutions = Institution(
            name=Institutions.name,
            slug = Institutions.slug,
            user_id = Institutions.user_id,
            created_at=Institutions.created_at
            # manager_id=Department.manager_id
            # ethnicity_id=Department.ethnicity_id

        )

        db.add(db_institutions)
        db.commit()
        db.refresh(db_institutions)
        
        return db_institutions
    @staticmethod
    def update_institutions(institution_id: int, institucion: InstitutionUpdate, db: Session = Depends(get_db)):
        db_institutions = db.query(Institution).filter(Institution.deleted_at == None, Institution.id == institution_id).first()

        if db_institutions:
            if institucion.name is not None:
                db_institutions.name = institucion.name
            if institucion.slug is not None:
                db_institutions.slug = institucion.slug
            if institucion.user_id is not None:
                db_institutions.user_id = institucion.user_id
            if institucion.updated_at is not None:
                db_institutions.updated_at = institucion.updated_at
            db.commit()
            db.refresh(db_institutions)

        return db_institutions

    
    @staticmethod
    def delete_institution(institution_id: int, db: Session):
        db_institution = db.query(Institution).filter(Institution.id == institution_id).first()

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