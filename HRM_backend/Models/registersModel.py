import re
from sqlalchemy import Column, Integer, String, DateTime, func, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from Config.database import Base
from passlib.hash import bcrypt
from datetime import datetime



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
    
    
class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    action = Column(String, index=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


# import logging
# from functools import wraps
# from sqlalchemy.orm import Session
# from fastapi import Depends
# from Models.registersModel import Log

# logger = logging.getLogger(__name__)

# def log_function_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         db: Session = kwargs.pop('db', None)

#         if db is None:
#             if 'db' in kwargs:
#                 db = kwargs['db']
#             elif args and isinstance(args[-1], Session):
#                 db = args[-1]
#                 args = args[:-1]

#         user_id = kwargs.get('user_id', 1)
#         entity_id = kwargs.get('entity_id')
#         entity_type = kwargs.get('entity_type')

#         try:
#             logger.info(f"User {user_id} is calling function: {func.__name__}")

#             initial_state = None
#             if entity_id and entity_type:
#                 initial_state = db.query(entity_type).filter(entity_type.id == entity_id).first()
#                 if initial_state:
#                     initial_state_repr = {column.name: getattr(initial_state, column.name) for column in initial_state.__table__.columns}
#                     logger.info(f"Initial state of {entity_type.__name__} with ID {entity_id}: {initial_state_repr}")

#             result = func(*args, **kwargs, db=db)
#             logger.info(f"Function {func.__name__} executed successfully by user {user_id}")

#             if entity_id and entity_type:
#                 updated_state = db.query(entity_type).filter(entity_type.id == entity_id).first()
#                 if updated_state:
#                     updated_state_repr = {column.name: getattr(updated_state, column.name) for column in updated_state.__table__.columns}
#                     logger.info(f"Updated state of {entity_type.__name__} with ID {entity_id}: {updated_state_repr}")

#                     changes = kwargs.get('changes', {})
#                     if changes:
#                         change_details = ", ".join([f"{k}: {v[0]} -> {v[1]}" for k, v in changes.items()])
#                         logger.info(f"Changes for {entity_type.__name__} with ID {entity_id}: {change_details}")

#                         # Save changes to the database log
#                         log_message = f"User {user_id} updated {entity_type.__name__} {entity_id}. Changes: {change_details}"
#                         log = Log(user_id=user_id, action=log_message)
#                         db.add(log)
#                         db.commit()

#             return result
#         except Exception as e:
#             logger.error(f"Function {func.__name__} called by user {user_id} failed with error: {e}", exc_info=True)
#             try:
#                 log = Log(user_id=user_id, action=f"Function {func.__name__} failed with error: {e}")
#                 db.add(log)
#                 db.commit()
#             except Exception as db_error:
#                 logger.error(f"Failed to log to database: {db_error}", exc_info=True)
#                 db.rollback()
#             raise
#     return wrapper

