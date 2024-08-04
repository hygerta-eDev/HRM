from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from .employee_rolesService import EmployeeRolesService
from Schema.employee_rolesSchema import EmployeeRolesCreate
from Config.database import get_db

router = APIRouter(prefix="/employeeRoles", tags=["EmployeeRoles"])

@router.get("/")
def get_all_employeeRoles(db: Session = Depends(get_db)):
    return EmployeeRolesService.get_all_employeeRoles(db=db)

@router.get("/by_role")
def get_employees_by_role(role_name: str, db: Session = Depends(get_db)):
    employees_with_role = EmployeeRolesService.get_all_employees_by_role(role_name, db)
    if not employees_with_role:
        raise HTTPException(status_code=404, detail="No employees found with this role")
    return employees_with_role
@router.get("/role_manager")
def get_role_manager_by_department(department_name: str, role_name: str, db: Session = Depends(get_db)):
    role_manager = EmployeeRolesService.get_role_manager_by_department(department_name, role_name, db)
    if not role_manager:
        raise HTTPException(status_code=404, detail="Role manager not found for the specified department and role")
    return role_manager

# @router.get("/{leaveType_id}")
# def get_leaveType_by_id(leaveType_id: int, db: Session = Depends(get_db)):
#     leaveType = LeaveTypeService.get_leaveType_by_id(db, leaveType_id)
#     if leaveType is None:
#         raise HTTPException(status_code=404, detail="LeaveType not found")
#     return leaveType

@router.post("/create_employeeRoles")
def create_employeeRoles(EmployeeRoles: EmployeeRolesCreate, db: Session = Depends(get_db)):
    return EmployeeRolesService.create_employeeRoles(EmployeeRoles, db)

# @router.put("/update_leaveType/{leaveType_id}")
# def update_leaveType(leaveType_id: int, leaveType: LeaveTypeUpdate, db: Session = Depends(get_db)):
#     return LeaveTypeService.update_leaveType(leaveType_id=leaveType_id, leaveType=leaveType, db=db)

# @router.delete("/delete_department/{leaveType_id}")
# def delete_department(leaveType_id: int, db: Session = Depends(get_db)):
#     return LeaveTypeService.delete_department(leaveType_id=leaveType_id, db=db)


@router.put("/update_employee_role/{employee_id}")
def update_employee_role(employee_id: int, role_name: str, db: Session = Depends(get_db)):
    try:
        employee_updated = EmployeeRolesService.update_employee_role(employee_id, role_name, db)
        if not employee_updated:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"message": f"Employee with ID {employee_id} role updated to {role_name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
