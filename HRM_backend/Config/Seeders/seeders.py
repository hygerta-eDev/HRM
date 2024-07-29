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
from Models.ethnicitiesModel import Ethnicities
from Models.DMS import DocumentCategory,Document
from Models.assessmentQuestionsModel import AssessmentQuestion  # Adjust import as needed
from Schema.enums.assessment_options import STANDARD_OPTIONS
from datetime import datetime
import json


def seed_initial_users(db: Session):
    if db.query(Users).count() == 0:
        users = [
            Users(name='Admin User', username='hg.admin', email='hg.admin@edev-rks.com', password='Password123', password_confirmation='Password123', active=True),
            # Users(name='User One', username='hg.user01', email='hg.user01@edev-rks.com', password='Password123', password_confirmation='Password123', active=True),
            # Users(name='User Two', username='hg.user02', email='hg.user02@edev-rks.com', password='Password123', password_confirmation='Password123', active=True)
        ]
        db.add_all(users)
        db.commit()

def seed_initial_institutions(db: Session):
    if db.query(Institution).count() == 0:
        institutions = [
            Institution(name='ETECH', slug='eTech', active=True, user_id=1),
            Institution(name='EDEV', slug='eDev', active=True, user_id=1),
            Institution(name='CYBERONE', slug='CyberOne', active=True, user_id=1)
        ]
        db.add_all(institutions)
        db.commit()

def seed_initial_departments(db: Session):
    if db.query(Departments).count() == 0:
        departments = [
            Departments(name='Systems', slug='Systems', active=True, institution_id=1, user_id=1),
            Departments(name='Network', slug='Network', active=True, institution_id=1, user_id=1),
            Departments(name='CyberSecurity', slug='CyberSecurity', active=True, institution_id=3, user_id=1),
            Departments(name='Department-edev-1', slug='Department-edev-1', active=True, institution_id=2, user_id=1),
            Departments(name='Department-edev-2', slug='Department-edev-2', active=True, institution_id=2, user_id=1),
            Departments(name='Department-edev-3', slug='Department-edev-3', active=True, institution_id=2, user_id=1)


        ]
        db.add_all(departments)
        db.commit()

def seed_initial_job_positions(db: Session):
    if db.query(JobPosition).count() == 0:
        job_positions = [
            JobPosition(name='System Engineering', slug='position-1',active=True, department_id=1, user_id=1),
            JobPosition(name='Network Engineering', slug='position-2',active=True, department_id=2, user_id=1),
            JobPosition(name='CyberSecurity', slug='position-3',active=True, department_id=3, user_id=1),
            JobPosition(name='Full Stack', slug='position-4',active=True, department_id=4, user_id=1)

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
            LeaveType(slug='annual_paid', limit=20),
            LeaveType(slug='sick', limit=20),
            LeaveType(slug='maternity', limit=364),
            LeaveType(slug='marriage', limit=5),
            LeaveType(slug='grief', limit=5),
            LeaveType(slug='birth_of_child', limit=3),
            LeaveType(slug='blood_giving', limit=1)
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
            Qualification(name='Bachelor', slug='qualification-1', user_id=1),
            Qualification(name='Master', slug='qualification-2', user_id=1),
            Qualification(name='Doktor Shkence ', slug='qualification-3', user_id=1)
        ]
        db.add_all(qualifications)
        db.commit()


def seed_initial_ethnicities(db: Session):
    if db.query(Ethnicities).count() == 0:
        ethnicities = [
            Ethnicities(name='Shqiptar', user_id=1),
            Ethnicities(name='Boshnjak', user_id=1),
            Ethnicities(name='Ethnicity C', user_id=1)
        ]
        db.add_all(ethnicities)
        db.commit()


def seed_document_categories(db: Session):
    if db.query(DocumentCategory).count() == 0:

        categories = [
            {
                "category_name": "Personal Information",
                "description": "Documents related to personal information",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "category_name": "Employment Details",
                "description": "Documents related to professional career",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "category_name": "Performance",
                "description": "Documents related to performance",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
                        {
                "category_name": "Training ",
                "description": "Documents related to trainings",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
                        {
                "category_name": "Legal Documents",
                "description": "Documents related to legal matters",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
                        {
                "category_name": "Other",
                "description": "Other category documents ",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
        ]
        for category in categories:
            db_category = DocumentCategory(**category)
            db.add(db_category)
        db.commit()
def seed_initial_assessment_questions(db: Session):
    if db.query(AssessmentQuestion).count() == 0:
        questions = [
            AssessmentQuestion(
                title="Cilësia e punës",
                description="Puna është përfunduar me saktësi (me pak ose aspak gabime), në mënyrë efikase dhe brenda afateve me mbikëqyrje minimale.",
                # weight=1,
                notes="null",
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Besueshmëria",
                description="Në vazhdimësi përformon në nivel të lartë, menaxhon kohën dhe ngarkesën e punës në mënyrë efektive duke i përmbushur përgjegjësitë.",
                # weight=1,
                notes="null",
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Gjykimi dhe vendimarrja",
                description="Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.",
                # weight=1,
                notes="null",
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Aftësitë komunikuese",
                description="Komunikimet me shkrim dhe me gojë janë te qarta, të organizuara dhe efektive. I dëgjon mire dhe kupton mire natyrën e problemeve.",
                # weight=1,
                notes="null",
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Iniciativa dhe fleksibiliteti",
                description="Demostron iniciativë, shpesh duke kërkuar përgjegjësi shtesë, identifikon probemet dhe zgjidhjet. Përshtatet me sfidat e reja dhe ndryshimet e papritura.",
                # weight=1,
                notes="null",
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Bashkëpunimi dhe puna ekipore",
                description="Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.",
                # weight=1,
                notes="null",
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Njohuritë për pozitën e punës:",
                description="Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.",
                # weight=1,
                notes="null",
                options=json.dumps(STANDARD_OPTIONS) 
            ),
            AssessmentQuestion(
                title="Trajnimi dhe zhvillimi",
                description="Vazhdimisht kërkon mënyra për të forcuar performancën dhe monitoron rregullisht zhvillimet e reja në fushën e punës.",
                # weight=1,
                notes="null",
                options=json.dumps(STANDARD_OPTIONS) 
            ),

        ]
        db.add_all(questions)
        db.commit()
# def seed_documents(db: Session):
#     if db.query(Document).count() == 0:

#         documents = [
#             {
#                 "title": "passport",
#                 "description": "Employee passport",
#                 "file_path": "/path/to/passport.pdf",
#                 "employee_id": 1,
#                 "category_id": 1
#             },
#             {
#                 "title": "employment_contracts",
#                 "description": "Employment contract",
#                 "file_path": "/path/to/contract.pdf",
#                 "employee_id": 1,
#                 "category_id": 2
#             }
#         ]
#         for document in documents:
#             db_document = Document(**document)
#             db.add(db_document)
#         db.commit()



def seed_all(db: Session):
    seed_initial_users(db)
    seed_initial_institutions(db)
    seed_initial_departments(db)
    seed_initial_job_positions(db)
    seed_initial_roles(db)
    seed_initial_leave_types(db)
    seed_initial_holidays(db)
    seed_initial_qualifications(db)
    seed_initial_ethnicities(db)
    seed_document_categories(db)
    seed_initial_assessment_questions(db)

    # seed_documents(db)