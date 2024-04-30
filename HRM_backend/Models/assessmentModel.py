from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Config.database import Base

class Assessment(Base):
    __tablename__ = 'assessments'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    job_position_id = Column(Integer, ForeignKey('job_positions.id'))
    evaluation_period = Column(Text)
    rate = Column(Float, default=0)
    finished = Column(Boolean, default=False)
    status = Column(String, default='created')
    performance_objectives = Column(Text)
    general_evaluation = Column(Text)
    employee_notes = Column(Text)
    employee_notes_date = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    employee = relationship("Employees", back_populates="assessments")
    job_position = relationship("JobPosition", back_populates="assessments")
    assessment_questions = relationship("AssessmentQuestion", back_populates="assessment")

    # hr_employee = relationship("HREmployees", back_populates="assessments")
    # user = relationship("User", back_populates="assessments")
