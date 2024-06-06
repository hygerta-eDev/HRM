from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from Config.database import Base
from sqlalchemy.orm import relationship

class LeaveType(Base):
    __tablename__ = 'leave_types'

    id = Column(Integer, primary_key=True)
    slug = Column(String)
    limit = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)
    leaves = relationship("Leaves", back_populates="leave_type")
    employee_leave_quota = relationship("EmployeeLeaveQuota", back_populates="leave_type")
    
    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None

    # def __repr__(self):
    #     return f"<LeaveType(id={self.id}, slug={self.slug}, limit={self.limit})>"
