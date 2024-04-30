from sqlalchemy import Column, ForeignKey, Integer, String, Date
from Config.database import Base
from sqlalchemy.orm import relationship

class Test(Base):
    __tablename__ = "test"

    department_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)