# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from Config.database import Base


# class Log(Base):
#     __tablename__ = 'logs'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
#     action = Column(String, index=True, nullable=False)
#     timestamp = Column(DateTime, default=datetime.utcnow)
#     # user = relationship("User", back_populates="logs")
#     def __repr__(self):
#         return f"<Log(id={self.id}, slug={self.slug}, limit={self.limit})>"