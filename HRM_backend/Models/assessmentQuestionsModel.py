from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey,DateTime,func
from sqlalchemy.orm import relationship
from Config.database import Base


class AssessmentQuestion(Base):
    __tablename__ = 'assessment_questions'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    options = Column(Text)
    weight = Column(Float)
    selected_option = Column(String)
    notes = Column(Text)
    assessment_id = Column(Integer, ForeignKey('assessments.id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    assessment = relationship("Assessment", back_populates="assessment_questions")
    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None
