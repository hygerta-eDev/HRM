from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,func
from sqlalchemy.orm import relationship
from Config.database import Base

class EmployeeTraining(Base):
    __tablename__ = 'employee_training'

    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    training_id = Column(Integer, ForeignKey('trainings.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    # Define relationship with Employees and Training tables
    employee = relationship("Employees", back_populates="employee_training")
    training = relationship("Training", back_populates="employee_training")

    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None
