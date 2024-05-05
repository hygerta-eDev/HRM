from enum import Enum

class MaritalStatus(str, Enum):
    Single = 'Single'
    Married = 'Married'
    Divorced = 'Divorced'
    Widowed = 'Widowed'