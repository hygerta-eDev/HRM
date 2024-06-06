from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Config.database import Base

class Departments(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    active = Column(Boolean)
    institution_id = Column(Integer, ForeignKey('institutions.id'))    
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    employees = relationship("Employees", back_populates="departments")
    job_positions = relationship("JobPosition", back_populates="department")
    institucion = relationship("Institution", back_populates="departments")  # Fixed relationship definition


    def soft_delete(self):
        self.deleted_at = func.now()

    # Method to check if the instance is deleted
    def is_deleted(self):
        return self.deleted_at is not None

    # ethnicity_id = Column(Integer, ForeignKey('ethnicity.id'))
    # ethnicity = relationship("Ethnicities", back_populates="departments")
