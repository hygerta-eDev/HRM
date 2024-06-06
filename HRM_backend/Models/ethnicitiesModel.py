from sqlalchemy import Column, Integer, String, DateTime, func, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from Config.database import Base


class Ethnicities(Base):
    __tablename__ = 'ethnicity'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    employees = relationship("Employees", back_populates="ethnicity")
    # departments = relationship("Departments", back_populates="ethnicity")
    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None