from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime,LargeBinary,ARRAY
from sqlalchemy.orm import relationship
from Config.database import Base
from .departmentsModel import Departments
from .ethnicitiesModel import Ethnicities
from .jobPositionModel import JobPosition
import pickle

# from .leavesModel import Leaves

class Employees(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String, unique=True, index=True)
    username = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    gender = Column(String, default='N/A')
    ethnicity_id = Column(Integer, ForeignKey('ethnicity.id'))
    marital_status = Column(String, default='single')
    date_of_birth = Column(Date)
    date_hired = Column(Date)
    contract_end_date = Column(Date)
    institucion_id = Column(Integer, ForeignKey('institutions.id'))
    department_id = Column(Integer, ForeignKey('departments.id'))
    personal_number = Column(String, unique=True, index=True)
    salary = Column(String, default='0')
    addition = Column(Integer, default=0)
    job_position_id = Column(Integer, ForeignKey('job_positions.id'))
    street = Column(String)
    city = Column(String)
    zipcode = Column(String)
    country = Column(String)
    phone_number = Column(String)
    phone_number_2 = Column(String)
    email = Column(String)
    email_2 = Column(String)
    days_off = Column(Integer, default=0)
    transferred_days_off = Column(Integer, default=0)
    earned_days_off = Column(Integer, default=0)
    next_year_earned_days_off = Column(Integer, default=2028)
    work_contract_termination_date = Column(Date, nullable=True)
    termination_reason_id = Column(Integer, ForeignKey('WorkTerminationReason.id'))
    active = Column(Boolean, default=True)
    qualification_id = Column(Integer, ForeignKey('qualifications.id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    # cv = Column(LargeBinary)
    # documents = Column(ARRAY(LargeBinary))
    the_workouts_selection = Column(String) #(Primar apo Sekondar)  

    created_at =Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at= Column(DateTime)
    
    ethnicity = relationship("Ethnicities", back_populates="employees")
    departments = relationship("Departments", back_populates="employees")
    institucion = relationship("Institution", back_populates="employees")

    job_positions = relationship("JobPosition", back_populates="employees")
    WorkTerminationReason = relationship("TerminationReason", back_populates="employees")
    qualifications = relationship("Qualification", back_populates="employees")
    
    employee_work_experience = relationship("WorkExperience", back_populates="employee")
    assessments = relationship("Assessment", back_populates="employee")
    employee_training = relationship("EmployeeTraining", back_populates="employee")
    # leaves = relationship("Leaves", back_populates="employee")
    leaves = relationship("Leaves", back_populates="employee")
    employee_leave_quota = relationship("EmployeeLeaveQuota", back_populates="employee")
    employee_roles = relationship("EmployeeRoles", back_populates="employee")


    documents = relationship("Document", back_populates="creator")
    document_versions = relationship("DocumentVersion", back_populates="creator")
    document_access = relationship("DocumentAccess", back_populates="employee", foreign_keys="[DocumentAccess.employee_id]")
    document_audits = relationship("DocumentAudit", back_populates="employee", foreign_keys="[DocumentAudit.employee_id]")
    granted_access = relationship("DocumentAccess", back_populates="granter", foreign_keys="[DocumentAccess.granted_by]")


    # def set_documents(self, documents):
    #     self.documents = pickle.dumps(documents)

    # def get_documents(self):
    #     return pickle.loads(self.documents) if self.documents else []

# class Employees(Base):
#     __tablename__ = 'employees'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     number = Column(String, unique=True, index=True)
#     username = Column(String)
#     middle_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String, default='N/A')
#     ethnicity_id = Column(Integer, ForeignKey('ethnicity.id'))
#     marital_status = Column(String, default='single')
#     # driving_license = Column(String)
#     date_of_birth = Column(Date)
#     date_hired = Column(Date)
#     contract_end_date = Column(Date)
#     department_id = Column(Integer, ForeignKey('departments.id'))
#     personal_number = Column(String, unique=True, index=True)
#     salary = Column(String, default='0')
#     # salary_coefficient = Column(String, default='0')
#     addition = Column(Integer, default=0)
#     # job_position_id = Column(Integer, ForeignKey('job_positions.id'))
#     street = Column(String)
#     city = Column(String)
#     zipcode = Column(String)
#     country = Column(String)
#     phone_number = Column(String)
#     phone_number_2 = Column(String)
#     email = Column(String)
#     email_2 = Column(String)
#     days_off = Column(Integer, default=0)
#     transferred_days_off = Column(Integer, default=0)
#     earned_days_off = Column(Integer, default=0)
#     next_year_earned_days_off = Column(Integer, default=2028)
#     work_contract_termination_date = Column(Date, nullable=True)
#     # termination_reason_id = Column(Integer, ForeignKey('termination_reasons.id'))
#     # manager_id = Column(Integer, ForeignKey('employees.id'))
#     active = Column(Boolean, default=True)
#     # qualification_id = Column(Integer, ForeignKey('qualifications.id'))
#     user_id = Column(Integer, ForeignKey('users.user_id'))
#     # bank_account = Column(String)
#     # bank_id = Column(Integer, ForeignKey('banks.id'))
#     ethnicity = relationship("Ethnicities", back_populates="employees")

#     departments = relationship("Departments", back_populates="employees")
#     # job_position = relationship("JobPosition")
#     # termination_reason = relationship("TerminationReason")
#     # qualification = relationship("EmployeeQualification")
#     # user = relationship("User")
