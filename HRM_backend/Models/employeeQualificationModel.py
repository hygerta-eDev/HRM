from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from Config.database import Base

class Qualification(Base):
    __tablename__ = 'qualifications'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    employees = relationship("Employees", back_populates="qualifications")
    # employee_id = Column(Integer, ForeignKey('employees.id'))
    # employee = relationship("Employee", back_populates="employee_qualification")
    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None
