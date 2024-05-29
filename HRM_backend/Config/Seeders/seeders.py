from sqlalchemy.orm import Session
from Config.database import engine
from Models.institutionModel import Institution
from Models.registersModel import Users
from Models.departmentsModel import Departments
from Models.jobPositionModel import JobPosition 
from Models.rolesModel import Roles
from Models.leaveTypeModel import LeaveType
from Models.holidayModel import Holiday 
from Models.employeeQualificationModel import Qualification

def seed_initial_users(db: Session):
    if db.query(Users).count() == 0:
        users = [
            Users(name='Admin User', username='admin', email='admin@edev-rks.com', password='hashed_passworD123', password_confirmation='hashed_password', active=True),
            Users(name='User One', username='user1', email='user1@edev-rks.com', password='hashed_passworD123', password_confirmation='hashed_password', active=True),
            Users(name='User Two', username='user2', email='user2@edev-rks.com', password='hashed_passworD123', password_confirmation='hashed_password', active=True)
        ]
        db.add_all(users)
        db.commit()

def seed_initial_institutions(db: Session):
    if db.query(Institution).count() == 0:
        institutions = [
            Institution(name='Institution A', slug='institution-a', active=True, user_id=1),
            Institution(name='Institution B', slug='institution-b', active=True, user_id=1),
            Institution(name='Institution C', slug='institution-c', active=True, user_id=1)
        ]
        db.add_all(institutions)
        db.commit()

def seed_initial_departments(db: Session):
    if db.query(Departments).count() == 0:
        departments = [
            Departments(name='Department 1', slug='department-1', active=True, institution_id=1, user_id=1),
            Departments(name='Department 2', slug='department-2', active=True, institution_id=1, user_id=1),
            Departments(name='Department 3', slug='department-3', active=True, institution_id=1, user_id=1)
        ]
        db.add_all(departments)
        db.commit()

def seed_initial_job_positions(db: Session):
    if db.query(JobPosition).count() == 0:
        job_positions = [
            JobPosition(name='Position 1', slug='position-1',active=True, department_id=1, user_id=1),
            JobPosition(name='Position 2', slug='position-2',active=True, department_id=2, user_id=1),
            JobPosition(name='Position 3', slug='position-3',active=True, department_id=3, user_id=1)
        ]
        db.add_all(job_positions)
        db.commit()
def seed_initial_roles(db: Session):
    if db.query(Roles).count() == 0:
        roles = [
            Roles(name='Admin'),
            Roles(name='Manager'),
            Roles(name='Employee')
        ]
        db.add_all(roles)
        db.commit()
def seed_initial_leave_types(db: Session):
    if db.query(LeaveType).count() == 0:
        leave_types = [
            LeaveType(slug='annual', limit=20),
            LeaveType(slug='sick', limit=10),
            LeaveType(slug='maternity', limit=15)
        ]
        db.add_all(leave_types)
        db.commit()

def seed_initial_holidays(db: Session):
    if db.query(Holiday).count() == 0:
        holidays = [
            Holiday(date='2024-12-25', recurring=1, description='Christmas'),
            Holiday(date='2024-01-01', recurring=1, description='New Year'),
            Holiday(date='2024-02-17', recurring=1, description='Independence Day')
        ]
        db.add_all(holidays)
        db.commit()
def seed_initial_qualifications(db: Session):  # Added seed function for Qualifications
    if db.query(Qualification).count() == 0:
        qualifications = [
            Qualification(name='Qualification 1', slug='qualification-1', user_id=1),
            Qualification(name='Qualification 2', slug='qualification-2', user_id=1),
            Qualification(name='Qualification 3', slug='qualification-3', user_id=1)
        ]
        db.add_all(qualifications)
        db.commit()

def seed_all(db: Session):
    seed_initial_users(db)
    seed_initial_institutions(db)
    seed_initial_departments(db)
    seed_initial_job_positions(db)
    seed_initial_roles(db)
    seed_initial_leave_types(db)
    seed_initial_holidays(db)
    seed_initial_qualifications(db)