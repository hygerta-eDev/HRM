from fastapi import APIRouter, Depends, HTTPException, Form,Query
from sqlalchemy.orm import Session
from .employeeService import EmployeeService
from Schema.employeeSchema import EmployeeCreate,EmployeeUpdate,UsernameRequest,UsernameResponse
from Config.database import get_db
from typing import List,Dict
from Schema.enums.Marital_status import MaritalStatus
from Schema.enums.genders import Genders
from Schema.enums.city import cities_data,CityResponse,City

router = APIRouter(prefix="/employees", tags=["Employee"])

@router.get("/")
def get_all_employees(db: Session = Depends(get_db)):
    return EmployeeService.get_all_employees(db=db)

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = EmployeeService.get_employee_by_id(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.post("/create_employee")
def create_employee(Employee: EmployeeCreate, db: Session = Depends(get_db)):
    return EmployeeService.create_employee(Employee, db)


# @router.put("/{employee_id}")
# def update_appointment(employee_id: int, Employee: EmployeeUpdate, db: Session = Depends(get_db)):
#     return EmployeeService.update_appointment(employee_id=employee_id, Employee=Employee, db=db)
# @router.put("/employees/{employee_id}/update_appointment")
# def update_employee_appointment(employee_id: int, employee_update: EmployeeUpdate, db: Session = Depends(get_db)):
#     db_employee = EmployeeService.get_employee_by_id(db, employee_id)
#     if db_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
    
#     # Update only the fields that are provided in the request
#     for field, value in employee_update.dict().items():
#         if value is not None:
#             setattr(db_employee, field, value)
    
#     db.commit()
#     db.refresh(db_employee)
    
#     return db_employee
@router.put("/update_employee/{employee_id}")
def update_employee(employee_id: int, Employee: EmployeeUpdate, db: Session = Depends(get_db)):
    return EmployeeService.update_employee(employee_id=employee_id, Employee=Employee, db=db)
@router.delete("/delete_employee/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return EmployeeService.delete_employee(employee_id=employee_id, db=db)

# @router.get("/marital_status", response_model=List[MaritalStatus])
# async def get_marital_status_options():
#     return [status.to_dict() for status in MaritalStatus]
@router.get("/marital_status", response_model=List[MaritalStatus])
async def read_marital_status():
    return list(MaritalStatus)

# @router.get("/genders", response_model=List[str])
# def get_genders_options():
#     genders_options = [status.value for status in Genders]
#     return genders_options

@router.get("/genders", response_model=List[Genders])
async def read_genders():
    return list(Genders)

@router.get("/check-number-exists")
def check_number_exists(number: str = Query(...), db: Session = Depends(get_db)):
    existing_employee = EmployeeService.get_employee_by_number(db, number)
    if existing_employee:
        return {"exists": True}
    else:
        return {"exists": False}

@router.get("/check-personal-number-exists")
def check_personal_number_exists(personal_number: str = Query(...), db: Session = Depends(get_db)):
    existing_employee = EmployeeService.get_employee_by_personal_number(db, personal_number)
    if existing_employee:
        return {"exists": True}
    else:
        return {"exists": False}
    

@router.get("/download/cv/{employee_id}")
def download_cv(employee_id: int, db: Session = Depends(get_db)):
    try:
        # Call the download_cv method of the service class
        return EmployeeService.download_cv(employee_id,db)
    except KeyError:
        raise HTTPException(status_code=404, detail="Employee not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@router.get("/last_employee_id")
def get_last_employee_id(db: Session = Depends(get_db)):
    return EmployeeService.get_last_employee_id(db=db)


@router.get("/cities", response_model=List[CityResponse])
async def get_cities():
    city_responses = [
        CityResponse(city_name=city_name, zip_codes=cities_data[city_name]) 
        for city_name in cities_data.keys()
    ]
    return city_responses

@router.get("/zipcodes", response_model=CityResponse)
def get_cities(city_name: str):
    if city_name not in cities_data:
        raise HTTPException(status_code=404, detail="City not found")
    zip_codes = cities_data[city_name]
    return CityResponse(city_name=city_name, zip_codes=zip_codes)

@router.get("/generate_unique_number")
def generate_unique_number(db: Session = Depends(get_db)):
    unique_number = EmployeeService.generate_unique_number(db)
    return {"number": unique_number}

@router.post("/generate-username", response_model=UsernameResponse)
def generate_username(request_data: UsernameRequest):
    if request_data.name and request_data.last_name:
        username = f"{request_data.name.lower()}.{request_data.last_name.lower()}"
        return {"username": username}
    else:
        return {"username": None}