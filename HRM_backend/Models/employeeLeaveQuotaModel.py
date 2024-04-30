from sqlalchemy import Column, Integer, ForeignKey, DECIMAL,DateTime
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
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    leave_type = relationship("LeaveType", back_populates="employee_leave_quota")
    employee = relationship("Employees", back_populates="employee_leave_quota")
    # leave_period = relationship("LeavePeriod", back_populates="employee_leave_quota")
