from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from Config.database import Base
from sqlalchemy.orm import relationship

class LeaveType(Base):
    __tablename__ = 'leave_types'

    id = Column(Integer, primary_key=True)
    slug = Column(String)
    limit = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)
    leaves = relationship("Leaves", back_populates="leave_type")
    employee_leave_quota = relationship("EmployeeLeaveQuota", back_populates="leave_type")

    # def __repr__(self):
    #     return f"<LeaveType(id={self.id}, slug={self.slug}, limit={self.limit})>"
