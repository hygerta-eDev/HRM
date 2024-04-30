from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from Config.database import Base


class Ethnicities(Base):
    __tablename__ = 'ethnicity'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employees", back_populates="ethnicity")
    # departments = relationship("Departments", back_populates="ethnicity")
