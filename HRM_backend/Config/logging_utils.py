# import logging
# from functools import wraps

# logger = logging.getLogger(__name__)

# def log_function_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         user_id = kwargs.get('user_id') or 'Unknown User'  # Adjust based on your auth mechanism
#         try:
#             logger.info(f"User {user_id} is calling function: {func.__name__}")
#             result = func(*args, **kwargs)
#             logger.info(f"Function {func.__name__} executed successfully by user {user_id}")
#             return result
#         except Exception as e:
#             logger.error(f"Function {func.__name__} called by user {user_id} failed with error: {e}", exc_info=True)
#             raise  # Re-raise the exception after logging it
#     return wrapper
        
            #Fixed part #

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
        
#         # Ensure db is provided
#         if db is None:
#             # Check if 'db' is passed as a keyword argument
#             if 'db' in kwargs:
#                 db = kwargs['db']
#             # Otherwise, check if it's provided as a positional argument
#             elif args and isinstance(args[-1], Session):
#                 db = args[-1]
#                 args = args[:-1]  # Remove the session from args

#         # Handle user_id extraction
#         user_id = kwargs.get('user_id', 1)  # Default to 1 if user_id is not provided

#         try:
#             logger.info(f"User {user_id} is calling function: {func.__name__}")
            
#             # Before calling the function, capture the initial state of the entity being updated
#             if 'entity_id' in kwargs and 'entity_type' in kwargs:
#                 entity_id = kwargs['entity_id']
#                 entity_type = kwargs['entity_type']
#                 entity = db.query(entity_type).filter(entity_type.id == entity_id).first()
#                 logger.info(f"Initial state of {entity_type.__name__} with ID {entity_id}: {entity}")

#             result = func(*args, **kwargs, db=db)
#             logger.info(f"Function {func.__name__} executed successfully by user {user_id}")

#             # Save to database
#             log = Log(user_id=user_id, action=f"Function {func.__name__} executed successfully by user {user_id}")
#             db.add(log)
#             db.commit()
#             return result
#         except Exception as e:
#             logger.error(f"Function {func.__name__} called by user {user_id} failed with error: {e}", exc_info=True)

#             # Save to database
#             try:
#                 log = Log(user_id=user_id, action=f"Function {func.__name__} failed with error: {e}")
#                 db.add(log)
#                 db.commit()
#             except Exception as db_error:
#                 logger.error(f"Failed to log to database: {db_error}", exc_info=True)
#                 db.rollback()
#             raise  # Re-raise the original exception after logging it
#     return wrapper


# import logging
# from functools import wraps
# from sqlalchemy.orm import Session
# from fastapi import Request
# from Models.registersModel import Log
# from fastapi import Depends, HTTPException

# logger = logging.getLogger(__name__)

# def log_function_call(func):
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         request: Request = kwargs.get('request')  # Get the request object from kwargs
        
#         # Ensure db is provided
#         db: Session = kwargs.pop('db', None)
#         if db is None:
#             raise ValueError("Database session is required")

#         # Extract user_id from request headers
#         user_id = request.headers.get('X-User-Id')
#         if user_id is None:
#             raise HTTPException(status_code=400, detail="User ID not provided in headers")

#         try:
#             logger.info(f"User {user_id} is calling function: {func.__name__}")
#             result = await func(*args, **kwargs, db=db, user_id=user_id)
#             logger.info(f"Function {func.__name__} executed successfully by user {user_id}")

#             # Save to database
#             log = Log(user_id=user_id, action=f"Function {func.__name__} executed successfully by user {user_id}")
#             db.add(log)
#             db.commit()
#             return result
#         except Exception as e:
#             logger.error(f"Function {func.__name__} called by user {user_id} failed with error: {e}", exc_info=True)

#             # Save to database
#             try:
#                 log = Log(user_id=user_id, action=f"Function {func.__name__} failed with error: {e}")
#                 db.add(log)
#                 db.commit()
#             except Exception as db_error:
#                 logger.error(f"Failed to log to database: {db_error}", exc_info=True)
#                 db.rollback()
#             raise  # Re-raise the original exception after logging it
#     return wrapper




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
#                 initial_state_repr = {column.name: getattr(initial_state, column.name) for column in initial_state.__table__.columns}
#                 logger.info(f"Initial state of {entity_type.__name__} with ID {entity_id}: {initial_state_repr}")

#             result = func(*args, **kwargs, db=db)
#             logger.info(f"Function {func.__name__} executed successfully by user {user_id}")

#             if entity_id and entity_type:
#                 updated_state = db.query(entity_type).filter(entity_type.id == entity_id).first()
#                 updated_state_repr = {column.name: getattr(updated_state, column.name) for column in updated_state.__table__.columns}
#                 logger.info(f"Updated state of {entity_type.__name__} with ID {entity_id}: {updated_state_repr}")

#                 changes = kwargs.get('changes', {})
#                 if changes:
#                     change_details = ", ".join([f"{k}: {v[0]} -> {v[1]}" for k, v in changes.items()])
#                     logger.info(f"Changes for {entity_type.__name__} with ID {entity_id}: {change_details}")
#                     log_message = f"User {user_id} updated {entity_type.__name__} {entity_id}. Changes: {change_details}"
#                     log = Log(user_id=user_id, action=log_message)
#                     db.add(log)
#                     db.commit()

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


            #  the last function that work #

# import logging
# from functools import wraps
# from sqlalchemy.orm import Session
# from fastapi import Depends, HTTPException
# from Models.registersModel import Log  # Assuming these models are imported correctly
# from Models.institutionModel import Institution
# from sqlalchemy import func
# from typing import Any

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
#         changes = kwargs.get('changes', {})

#         logger.debug(f"Wrapper invoked with: db={db}, user_id={user_id}, entity_id={entity_id}, entity_type={entity_type}, changes={changes}")

#         try:
#             logger.info(f"User {user_id} is calling function: {func.__name__}")
#             logger.debug(f"Function arguments: args={args}, kwargs={kwargs}")

#             if func.__name__.startswith('create_'):
#                 # Log creation details
#                 entity_data = args[0]
#                 logger.info(f"Creating new entity with data: {entity_data}")
#                 log_message = f"User {user_id} is creating new entity with data: {entity_data}"
#                 log = Log(user_id=user_id, action=log_message)
#                 db.add(log)
#                 db.commit()

#             result = func(*args, **kwargs, db=db)

#             if func.__name__.startswith('create_'):
#                 # Log the created entity's details
#                 created_entity = result
#                 entity_repr = {column.name: getattr(created_entity, column.name) for column in created_entity.__table__.columns}
#                 logger.info(f"Created entity: {entity_repr}")
#                 log_message = f"User {user_id} created new entity with details: {entity_repr}"
#                 log = Log(user_id=user_id, action=log_message)
#                 db.add(log)
#                 db.commit()

#             # elif func.__name__ == 'get_institution_by_id':
#             #     institution_id = kwargs.get('institution_id')
#             #     logger.info(f"Fetching Institution with ID: {institution_id}")
#             #     log_message = f"User {user_id} is fetching Institution with ID: {institution_id}"
#             #     log = Log(user_id=user_id, action=log_message)
#             #     db.add(log)
#             #     db.commit()
#             elif func.__name__.endswith('_by_id'):
#                 entity_id = kwargs.get('entity_id')
#                 logger.info(f"Fetching entity with ID: {entity_id}")
#                 log_message = f"User {user_id} is fetching entity with ID: {entity_id}"
#                 log = Log(user_id=user_id, action=log_message)
#                 db.add(log)
#                 db.commit()

#             elif entity_id and entity_type:
#                 initial_state = db.query(entity_type).filter(entity_type.id == entity_id).first()
#                 if initial_state:
#                     initial_state_repr = {column.name: getattr(initial_state, column.name) for column in initial_state.__table__.columns}
#                     logger.info(f"Initial state of {entity_type.__name__} with ID {entity_id}: {initial_state_repr}")

#                 updated_state = db.query(entity_type).filter(entity_type.id == entity_id).first()
#                 if updated_state:
#                     updated_state_repr = {column.name: getattr(updated_state, column.name) for column in updated_state.__table__.columns}
#                     logger.info(f"Updated state of {entity_type.__name__} with ID {entity_id}: {updated_state_repr}")

#                     if changes:
#                         change_details = ", ".join([f"{k}: {v[0]} -> {v[1]}" for k, v in changes.items()])
#                         logger.info(f"Changes for {entity_type.__name__} with ID {entity_id}: {change_details}")
#                         log_message = f"User {user_id} updated {entity_type.__name__} {entity_id}. Changes: {change_details}"
#                         log = Log(user_id=user_id, action=log_message)
#                         db.add(log)
#                         db.commit()
#                         logger.debug("Changes successfully logged to database")
#                     else:
#                         logger.debug("No changes detected")

#             return result
#         except Exception as e:
#             logger.error(f"Function {func.__name__} called by user {user_id} failed with error: {e}", exc_info=True)
#             try:
#                 log_message = f"Function {func.__name__} failed with error: {e}"
#                 log = Log(user_id=user_id, action=log_message)
#                 db.add(log)
#                 db.commit()
#             except Exception as db_error:
#                 logger.error(f"Failed to log to database: {db_error}", exc_info=True)
#                 db.rollback()
#             raise
#     return wrapper



import logging
from functools import wraps
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from Models.registersModel import Log
from sqlalchemy import func
from typing import Any, Callable

logger = logging.getLogger(__name__)

def log_function_call(entity_name: str = None):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Extract db from kwargs or args
            db = kwargs.get('db', None)
            if db is None:
                for arg in args:
                    if isinstance(arg, Session):
                        db = arg
                        break

            if not isinstance(db, Session):
                raise ValueError("Database session not provided or incorrect argument position.")

            user_id = kwargs.get('user_id', 1)
            entity_id = kwargs.get('entity_id')
            entity_type = kwargs.get('entity_type')
            changes = kwargs.get('changes', {})

            logger.debug(f"Wrapper invoked with: db={db}, user_id={user_id}, entity_id={entity_id}, entity_type={entity_type}, changes={changes}")

            try:
                logger.info(f"User {user_id} is calling function: {func.__name__}")
                logger.debug(f"Function arguments: args={args}, kwargs={kwargs}")

                if func.__name__.startswith('create_'):
                    entity_data = args[0]
                    logger.info(f"Creating new entity with data: {entity_data}")
                    log_message = f"User {user_id} is creating new entity with data: {entity_data}"
                    log = Log(user_id=user_id, action=log_message)
                    db.add(log)
                    db.commit()

                if func.__name__.startswith('delete_'):
                    logger.info(f"User {user_id} is deleting {entity_name} with ID: {entity_id}")
                    log_message = f"User {user_id} is deleting {entity_name} with ID: {entity_id}"
                    log = Log(user_id=user_id, action=log_message)
                    db.add(log)
                    db.commit()

                result = func(*args, **kwargs)

                if func.__name__.startswith('create_'):
                    created_entity = result
                    entity_repr = {column.name: getattr(created_entity, column.name) for column in created_entity.__table__.columns}
                    logger.info(f"Created entity: {entity_repr}")
                    log_message = f"User {user_id} created new entity with details: {entity_repr}"
                    log = Log(user_id=user_id, action=log_message)
                    db.add(log)
                    db.commit()

                if func.__name__.endswith('_by_id'):
                    logger.info(f"Fetching {entity_name} with ID: {entity_id}")
                    log_message = f"User {user_id} is fetching {entity_name} with ID: {entity_id}"
                    log = Log(user_id=user_id, action=log_message)
                    db.add(log)
                    db.commit()

                if entity_id and entity_type:
                    initial_state = db.query(entity_type).filter(entity_type.id == entity_id).first()
                    if initial_state:
                        initial_state_repr = {column.name: getattr(initial_state, column.name) for column in initial_state.__table__.columns}
                        logger.info(f"Initial state of {entity_type.__name__} with ID {entity_id}: {initial_state_repr}")

                    updated_state = db.query(entity_type).filter(entity_type.id == entity_id).first()
                    if updated_state:
                        updated_state_repr = {column.name: getattr(updated_state, column.name) for column in updated_state.__table__.columns}
                        logger.info(f"Updated state of {entity_type.__name__} with ID {entity_id}: {updated_state_repr}")

                        if changes:
                            change_details = ", ".join([f"{k}: {v[0]} -> {v[1]}" for k, v in changes.items()])
                            logger.info(f"Changes for {entity_type.__name__} with ID {entity_id}: {change_details}")
                            log_message = f"User {user_id} updated {entity_type.__name__} {entity_id}. Changes: {change_details}"
                            log = Log(user_id=user_id, action=log_message)
                            db.add(log)
                            db.commit()
                            logger.debug("Changes successfully logged to database")
                        else:
                            logger.debug("No changes detected")

                return result
            except Exception as e:
                logger.error(f"Function {func.__name__} called by user {user_id} failed with error: {e}", exc_info=True)
                try:
                    log_message = f"Function {func.__name__} failed with error: {e}"
                    log = Log(user_id=user_id, action=log_message)
                    db.add(log)
                    db.commit()
                except Exception as db_error:
                    logger.error(f"Failed to log to database: {db_error}", exc_info=True)
                    db.rollback()
                raise
        return wrapper
    return decorator
