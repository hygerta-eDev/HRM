from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Date,func
from sqlalchemy.orm import relationship
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
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    employee = relationship("Employees", back_populates="employee_work_experience")
    
    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None

