from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Config.database import Base

class Qualification(Base):
    __tablename__ = 'qualifications'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)

    employees = relationship("Employees", back_populates="qualifications")
    # employee_id = Column(Integer, ForeignKey('employees.id'))
    # employee = relationship("Employee", back_populates="employee_qualification")
