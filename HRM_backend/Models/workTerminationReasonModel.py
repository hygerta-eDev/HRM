from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from Config.database import Base


class TerminationReason(Base):
    __tablename__ = 'WorkTerminationReason'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    employees = relationship("Employees", back_populates="WorkTerminationReason")

