from sqlalchemy import Column, Integer, ForeignKey, DECIMAL,DateTime,func
from sqlalchemy.orm import relationship
from Config.database import Base

class EmployeeLeaveQuota(Base):
    __tablename__ = 'employee_leave_quota'

    leave_type_id = Column(Integer, ForeignKey('leave_types.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    # leave_period_id = Column(Integer, ForeignKey('leave_periods.id'), primary_key=True)
    amount = Column(DECIMAL(6, 2))
    taken = Column(DECIMAL(6, 2))
    available = Column(DECIMAL(6, 2))
    carried_over = Column(DECIMAL(6, 2))
    additional_approved = Column(DECIMAL(6, 2))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    leave_type = relationship("LeaveType", back_populates="employee_leave_quota")
    employee = relationship("Employees", back_populates="employee_leave_quota")


    def soft_delete(self):
        self.deleted_at = func.now()

    def is_deleted(self):
        return self.deleted_at is not None

    # leave_period = relationship("LeavePeriod", back_populates="employee_leave_quota")
