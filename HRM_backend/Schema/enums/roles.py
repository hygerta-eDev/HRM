from enum import Enum

class Roles(str, Enum):
    SuperAdmin = 'SuperAdmin'
    Admin = 'Admin'
    Manager = 'Manager'
    Employee = 'Employee'