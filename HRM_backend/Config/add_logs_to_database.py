from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from Config.database import SessionLocal, get_db
from Models.registersModel import Log

from sqlalchemy.orm import Session

def insert_data_into_db(db: Session, data: str):
    new_log = Log(log_entry=data)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, log_file, db_session_factory):
        self.log_file = log_file
        self.last_size = 0
        self.db_session_factory = db_session_factory

    def on_modified(self, event):
        if event.src_path == self.log_file:
            self.process_new_entries()

    def process_new_entries(self):
        with open(self.log_file, 'r') as f:
            f.seek(self.last_size)
            new_entries = f.readlines()
            self.last_size = f.tell()
            with self.db_session_factory() as db:
                for entry in new_entries:
                    insert_data_into_db(db, entry.strip())

def start_monitoring(log_file, db_session_factory):
    event_handler = LogFileHandler(log_file, db_session_factory)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
# if __name__ == "__main__":
#     log_file_path = 'path/to/your/logfile.log'  # Replace with your log file path
#     Base.metadata.create_all(bind=engine)  # Create tables
#     start_monitoring(log_file_path)


