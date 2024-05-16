from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from Config.database import Base
from Models.registersModel import Users
from Models.employeeModel import Employees
from Models.rolesModel import Roles

class EmployeeRoles(Base):
    __tablename__ = 'employee_roles'

    # id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))
    expires_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    # Define relationships
    role = relationship("Roles", back_populates="employee_roles")
    user = relationship("Users", foreign_keys=[user_id])
    employee = relationship("Employees", back_populates="employee_roles")

    __table_args__ = (
        PrimaryKeyConstraint('employee_id', 'role_id'),
    )