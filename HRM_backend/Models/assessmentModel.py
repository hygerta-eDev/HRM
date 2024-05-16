from sqlalchemy import Column, Integer, String, Float, Text,func, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
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
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    employee = relationship("Employees", back_populates="assessments")
    job_position = relationship("JobPosition", back_populates="assessments")
    assessment_questions = relationship("AssessmentQuestion", back_populates="assessment")

    # hr_employee = relationship("HREmployees", back_populates="assessments")
    # user = relationship("User", back_populates="assessments")
    
    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None