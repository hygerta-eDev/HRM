from enum import Enum
from typing import List
# from fastapi import FastAPI

# app = FastAPI()

class MaritalStatus(str, Enum):
    Single = 'Single'
    Married = 'Married'
    Divorced = 'Divorced'
    Widowed = 'Widowed'

