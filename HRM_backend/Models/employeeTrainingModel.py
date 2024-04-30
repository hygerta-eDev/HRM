from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Config.database import Base

class EmployeeTraining(Base):
    __tablename__ = 'employee_training'

    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    training_id = Column(Integer, ForeignKey('trainings.id'), primary_key=True)

    # Define relationship with Employees and Training tables
    employee = relationship("Employees", back_populates="employee_training")
    training = relationship("Training", back_populates="employee_training")