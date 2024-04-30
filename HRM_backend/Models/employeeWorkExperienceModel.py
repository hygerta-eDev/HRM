from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Config.database import Base

class WorkExperience(Base):
    __tablename__ = 'employee_work_experience'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start = Column(Date)
    type = Column(String, default='public')
    end = Column(Date)
    days = Column(Integer, default=0)
    employee_id = Column(Integer, ForeignKey('employees.id'))

    employee = relationship("Employees", back_populates="employee_work_experience")

