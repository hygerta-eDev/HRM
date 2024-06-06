from sqlalchemy.orm import Session
from Schema.DMS import DocumentBase, DocumentCreate,DocumentI,DocumentVersionCreate,DocumentVersion
from Models.DMS import Document,DocumentVersion,DocumentCategory,DocumentAccess,DocumentAudit,DocumentTagMap
from Models.employeeModel import Employees
from Config.database import get_db
from typing import List
from pathlib import Path
from fastapi import UploadFile
import aiofiles

# class DocumentTag(Base):
class DMSService:

    # Document CRUD
    def create_document(db: Session, document: DocumentCreate):
        db_document = Document(**document.dict())
        db.add(db_document)
        db.commit()
        db.refresh(db_document)
        return db_document

    def get_documents(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Document).offset(skip).limit(limit).all()

    def get_document(db: Session, document_id: int):
        return db.query(Document).filter(Document.document_id == document_id).first()

    def update_document(db: Session, document_id: int, document: DocumentBase):
        db_document = db.query(Document).filter(Document.document_id == document_id).first()
        if db_document:
            for key, value in document.dict().items():
                setattr(db_document, key, value)
            db.commit()
            db.refresh(db_document)
        return db_document

    def delete_document(db: Session, document_id: int):
        db_document = db.query(Document).filter(Document.document_id == document_id).first()
        if db_document:
            db.delete(db_document)
            db.commit()
        return db_document

    # def attach_documents_to_employee(db: Session, employee_id: int, documents_data: List[DocumentCreate]):
    #     attached_documents = []
    #     for document_data in documents_data:
    #         document = Document(**document_data.dict(), created_by=employee_id)
    #         db.add(document)
    #         db.commit()
    #         db.refresh(document)
    #         attached_documents.append(document)
    #     return attached_documents
    

    def attach_documents_to_employee(db: Session, employees_id: int, documents: List[UploadFile]):
        attached_documents = []
        for document_file in documents:
            # Save the file to a specified directory
            file_path = save_uploaded_file(document_file)

            # Create the document in the database
            document = Document(file_path=file_path, employee_id=employees_id)
            db.add(document)
            db.commit()
            db.refresh(document)
            attached_documents.append(document)
        return attached_documents
    def get_all_categories(db: Session):
        return db.query(DocumentCategory).all()
    
# def save_uploaded_file(file: UploadFile) -> str:
#     # Define the directory where files will be saved
#     upload_dir = Path("uploads")
#     upload_dir.mkdir(parents=True, exist_ok=True)
    
#     # Save the file with a unique name
#     file_path = upload_dir / file.filename
#     with file_path.open("wb") as buffer:
#         buffer.write(file.file.read())
#     return str(file_path)
async def save_uploaded_file(file: UploadFile) -> str:
    upload_dir = Path("uploads")  # Define the upload directory
    if not upload_dir.exists():
        upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / file.filename  # Construct the file path
    async with aiofiles.open(file_path, 'wb') as buffer:
        await buffer.write(await file.read())  # Write the file contents to the buffer

    return str(file_path)