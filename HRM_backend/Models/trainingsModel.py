from sqlalchemy import Column, Integer, String, Date, Text,func, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Config.database import Base

class Training(Base):
    __tablename__ = 'trainings'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(Text)
    outcome = Column(Text)
    active = Column(Boolean)
    completed_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    
    employee_training = relationship("EmployeeTraining", back_populates="training")

    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None
