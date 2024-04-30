
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

from Config.database import engine
from Config.database import Base

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return "Hello"

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






