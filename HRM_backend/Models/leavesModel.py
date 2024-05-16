from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship
from Config.database import Base
from Models.registersModel import Users
from Models.employeeModel import Employees
class Leaves(Base):
    __tablename__ = 'leaves'

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    days = Column(Integer, default=0)
    leave_type_id = Column(Integer, ForeignKey('leave_types.id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    approved_by_id = Column(Integer, ForeignKey('users.user_id'))
    approved_at = Column(DateTime)
    rejected_by_id = Column(Integer, ForeignKey('users.user_id'))
    rejected_at = Column(DateTime)
    rejected_comment = Column(String)
    status = Column(String, default='Inactive')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    # Define relationships
    leave_type = relationship("LeaveType", back_populates="leaves")
    user = relationship("Users", foreign_keys=[user_id])
    employee = relationship("Employees", back_populates="leaves")
    approved_by = relationship("Users", foreign_keys=[approved_by_id])
    rejected_by = relationship("Users", foreign_keys=[rejected_by_id])

    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None

