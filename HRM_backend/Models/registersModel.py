import re
from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from Config.database import Base
from passlib.hash import bcrypt


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True, index=True)
    email = Column(String)
    email_verified_at = Column(DateTime(timezone=True), default=None, onupdate=func.now())
    password = Column(String)  # Store the hashed password
    password_confirmation = Column(String)  # Store the hashed password confirmation
    active = Column(Boolean, default=True)
    banned_until = Column(DateTime)
    language = Column(String)
    
    # Regex pattern for password validation
    PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_=+]).{8,}$')

    def validate_password(self, password):
        """
        Validate the password against a regex pattern.
        """
        return bool(self.PASSWORD_REGEX.match(password))

    def hash_password(self, password):
        """
        Hash the password using bcrypt.
        """
        return bcrypt.hash(self.password)

    def hash_password_confirmation(self, password_confirmation):
        """
        Hash the password confirmation using bcrypt.
        """
        return bcrypt.hash(self.password_confirmation)
