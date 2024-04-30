from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
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

    assessment = relationship("Assessment", back_populates="assessment_questions")
