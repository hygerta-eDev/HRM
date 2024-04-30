from sqlalchemy import Column, Integer, String, Date, Text, Boolean, DateTime, ForeignKey
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
    user_id = Column(Integer, ForeignKey('users.user_id'))  # Assuming users table has a primary key 'id'
    active = Column(Boolean)
    completed_at = Column(DateTime)
    created_at =Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at= Column(DateTime)
    
    employee_training = relationship("EmployeeTraining", back_populates="training")

