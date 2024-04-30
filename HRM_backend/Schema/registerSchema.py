from pydantic import BaseModel, constr, validator
import re
from datetime import datetime
from passlib.hash import bcrypt
from Config.database import get_db
from typing import Optional
from .enums.language import Language

# Pydantic model with password hashing
class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    email_verified_at: datetime
    password: constr(min_length=8)
    password_confirmation: constr(min_length=8)
    active: bool
    banned_until: Optional[datetime]
    language: Language

    @validator("password_confirmation")
    def passwords_match(cls, v, values, **kwargs):
        """
        Validate that the password and password confirmation match.
        """
        if "password" in values and v != values["password"]:
            raise ValueError("passwords do not match")
        return v

    @validator("password")
    def password_regex_validation(cls, v):
        """
        Validate the password against a regex pattern.
        """
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_=+]).{8,}$', v):
            raise ValueError("password must contain at least one digit, one lowercase letter, "
                             "one uppercase letter, one special character, and be at least 8 characters long")
        return v
    @validator("email")
    def email_validation(cls, v):
        """
        Validate email format and domain.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@(edev-rks\.com|etech-rks\.com)$'
        if not re.match(email_regex, v):
            raise ValueError("invalid email format or domain")
        return v

