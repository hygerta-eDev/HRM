from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Config.database import Base

class Departments(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)

    employees = relationship("Employees", back_populates="departments")
    job_positions = relationship("JobPosition", back_populates="department")

    # ethnicity_id = Column(Integer, ForeignKey('ethnicity.id'))
    # ethnicity = relationship("Ethnicities", back_populates="departments")
