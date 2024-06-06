from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship
from Config.database import Base

class Holiday(Base):
    __tablename__ = 'holidays'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    recurring = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    description = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    
    
    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None
