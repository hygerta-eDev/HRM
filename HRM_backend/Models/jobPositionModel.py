from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Config.database import Base


class JobPosition(Base):
    __tablename__ = 'job_positions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    department = relationship("Departments", back_populates="job_positions")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    employees = relationship("Employees", back_populates="job_positions")
    assessments = relationship("Assessment", back_populates="job_position")
    
    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None

