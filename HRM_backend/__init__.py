import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from threading import Thread

from Config.database import SessionLocal, engine, Base, get_db
from Models.registersModel import Log
from sqlalchemy.orm import Session

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the table
Base.metadata.create_all(bind=engine)

# Function to insert data into the database
def insert_data_into_db(db: Session, data: str):
    new_log = Log(log_entry=data)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    logger.info(f"Inserted log entry: {data}")

# Class to handle file changes
class LogFileHandler(FileSystemEventHandler):
    def __init__(self, log_file, db_session_factory):
        self.log_file = log_file
        self.last_size = 0
        self.db_session_factory = db_session_factory

    def on_modified(self, event):
        logger.info(f"Detected file modification event: {event}")
        if event.src_path == self.log_file:
            logger.info(f"File modified: {self.log_file}")
            self.process_new_entries()

    def process_new_entries(self):
        with open(self.log_file, 'r') as f:
            f.seek(self.last_size)
            new_entries = f.readlines()
            self.last_size = f.tell()
            logger.info(f"New entries found: {new_entries}")
            with self.db_session_factory() as db:
                for entry in new_entries:
                    insert_data_into_db(db, entry.strip())

def start_monitoring(log_file, db_session_factory):
    event_handler = LogFileHandler(log_file, db_session_factory)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    logger.info(f"Started monitoring log file: {log_file}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    log_file_path = r'C:\Users\hygerta.hulaj\Desktop\HRM\HRM\HRM_backend\app.log'  # Raw string to fix the path issue

    # Run file monitoring in a separate thread
    monitor_thread = Thread(target=start_monitoring, args=(log_file_path, SessionLocal))
    monitor_thread.daemon = True
    monitor_thread.start()