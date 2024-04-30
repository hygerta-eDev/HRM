from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Config.database import Base

class Holiday(Base):
    __tablename__ = 'holidays'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    recurring = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
