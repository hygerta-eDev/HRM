from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from .logs import logger  # Import the logger
from sqlalchemy.orm import Session
from .database import get_db
from Models.registersModel import Log
import logging

class LogUserActionsMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, db_session_factory):
        super().__init__(app)
        self.db_session_factory = db_session_factory

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        user_id = request.headers.get('X-User-Id')  # Adjust based on your auth mechanism
        if user_id:
            db = next(self.db_session_factory())
            log = Log(user_id=user_id, action=request.url.path)
            db.add(log)
            db.commit()
        return response
    # def get_log_message(self):
    #     # You can modify this method based on your requirements to extract relevant log messages
    #     log_records = logging.getLogger().handlers[0].stream.getvalue()  # Assumes the first handler is for the log file
    #     return log_records
    def get_log_messages(self):
        log_messages = ""
        for handler in logging.getLogger().handlers:
            log_messages += handler.stream.getvalue()
        return log_messages