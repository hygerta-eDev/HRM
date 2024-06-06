
import pathlib

from starlette.requests import Request
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Services.test import testrouter
from Services.Register import registerRouter
from Services.Ethnicity import ethnicityRouter
from Services.Departments import departmentsRouter
from Services.Employee import employeeRouter
from Services.Job_position import job_positionRouter
from Services.WorkTerminationReason import work_termination_reasonRouter
from Services.Employee_qualification import  employee_qualificationRouter
from Services.Employee_Work_Experience import employee_work_experienceRouter
from Services.Assessment import assessmentRouter
from Services.Assessment_question import assessment_questionRouter
from Services.Trainings import trainingsRouter
from Services.Leave_type import leave_typeRouter
from Services.Leaves import leaveRouter
from Services.Holiday import holidayRouter
from Services.Leave_quota import leave_quotaRoute
from Services.Roles import rolesRouter
from Services.Employee_Roles import employee_rolesRouter
from Services.Institucions import institutionsRouter
from Services.DMS import dmsRouter
from Models.registersModel import Log
from Config.Seeders.seeders import seed_all

# from sqlalchemy import event
# from Models.leaveTypeModel import LeaveType
from Config.database import engine, Base,get_db
from Config.middleware import LogUserActionsMiddleware
from fastapi import Depends
from sqlalchemy.orm import Session


# app.add_middleware(LogExceptionsMiddleware)

from Config.logs import logger
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LogUserActionsMiddleware, db_session_factory=get_db)


# @app.on_event("startup")
# def configure():
#     Base.metadata.create_all(bind=engine)

# Base.metadata.create_all(engine)
    # from sqlalchemy import event
# from Models.institutionModel import Institution
# from Config.Seeders.institutionSeed import on_after_create

# # Bind the event listener
# event.listen(Institution.__table__, 'after_create', on_after_create)
# @app.middleware("http")
# async def log_user_actions_middleware(request: Request, call_next):
#     response = await call_next(request)
#     user_id = request.headers.get('X-User-Id')  # Adjust based on your auth mechanism
#     if user_id:
#         db_session = next(get_db())
#         log = Log(user_id=user_id, action=request.url.path)
#         db_session.add(log)
#         db_session.commit()
#     return response




# @app.get("/test1212")
# def read_root(db: Session = Depends(get_db), request: Request = None):
#     user_id = request.headers.get('X-User-Id')  # Adjust based on your auth mechanism
#     if user_id:
#         log = Log(user_id=user_id, action="Root endpoint called")
#         db.add(log)
#         db.commit()
#     logger.info("Root endpoint called")
#     return {"message": "Hello, World!"}

# @app.get("/helloo")
# def read_root(request: Request = None):
#     user_id = request.headers.get('X-User-Id')  # Adjust based on your auth mechanism
#     if user_id:
#         logger.info(f"Root endpoint called by user {user_id}")
#     else:
#         logger.info("Root endpoint called by an unknown user")
#     return {"message": "Hello, World!"}

# @app.get("/perform_action")
# def perform_action(user_id: int, db: Session = Depends(get_db)):
#     log = Log(user_id=user_id, action=f"Root endpoint called by user {user_id}")
#     db.add(log)
#     db.commit()
#     logger.info(f"Root endpoint called by user {user_id}")
#     return {"message": "Action performed"}




# @app.get("/test1212")
# def read_root(db: Session = Depends(get_db), request: Request = None):
#     user_id = request.headers.get('X-User-Id')  # Adjust based on your auth mechanism
#     if user_id:
#         log = Log(user_id=user_id, action="Root endpoint called")
#         db.add(log)
#         db.commit()
#     return {"message": "Hello, World!"}
# @app.get("/helloo")
# def read_root():
#     logger.info("Root endpoint called")
#     return {"message": "Hello, World!"}
# @app.get("/perform_action")
# def perform_action(user_id: int, db: Session = Depends(get_db)):
#     # Perform some action here
#     log = Log(user_id=user_id, action="Performed an action")
#     db.add(log)
#     db.commit()
#     return {"message": "Action performed"}

app.include_router(testrouter.router)
app.include_router(registerRouter.router)
app.include_router(ethnicityRouter.router)
app.include_router(departmentsRouter.router)
app.include_router(employeeRouter.router)
app.include_router(job_positionRouter.router)
app.include_router(work_termination_reasonRouter.router)
app.include_router(employee_qualificationRouter.router)
app.include_router(employee_work_experienceRouter.router)
app.include_router(assessmentRouter.router)
app.include_router(assessment_questionRouter.router)
app.include_router(trainingsRouter.router)
app.include_router(leave_typeRouter.router)
app.include_router(leaveRouter.router)
app.include_router(holidayRouter.router)
app.include_router(leave_quotaRoute.router)
app.include_router(rolesRouter.router)
app.include_router(employee_rolesRouter.router)
app.include_router(institutionsRouter.router)
app.include_router(dmsRouter.router)


def create_tables_and_seed():
    # Create tables
    Base.metadata.create_all(engine)
    
    # Seed initial data
    with Session(engine) as session:
        seed_all(session)
        # seed_initial_users(session)

        # seed_initial_data(session)

# Event handler for startup
@app.on_event("startup")
async def on_startup():
    create_tables_and_seed()