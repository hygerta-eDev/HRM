from fastapi import APIRouter, Depends, HTTPException,UploadFile,File,Body,Form,Query
from fastapi.responses import JSONResponse,FileResponse
from pathlib import Path
from sqlalchemy.orm import Session
from typing import List
from Config.database import Base,get_db
from Schema.DMS import DocumentBase, DocumentCreate,DocumentI,DocumentVersionCreate,DocumentVersion,DocumentCategorys,Documentss,DocumentOut,TitleResponse
from .dmsService import DMSService,save_uploaded_file
from Schema.enums.documents_title import CATEGORY_TITLE_MAPPING
import aiofiles
from datetime import datetime
from Models.DMS import Document,DocumentCategory
import zipfile
from tempfile import NamedTemporaryFile
import json
from typing import Optional,Annotated,Dict,Union
from pydantic import BaseModel,Field
from fastapi.responses import FileResponse
from starlette.requests import Request
import os

router = APIRouter()

@router.post("/", response_model=DocumentI)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    return DMSService.create_document(db=db, document=document)

@router.get("/", response_model=List[DocumentI])
def read_documents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    documents = DMSService.get_documents(db, skip=skip, limit=limit)
    return documents

# @router.get("/{document_id}", response_model=Document)
# def read_document(document_id: int, db: Session = Depends(get_db)):
#     db_document = DMSService.get_document(db, document_id=document_id)
#     if db_document is None:
#         raise HTTPException(status_code=404, detail="Document not found")
#     return db_document

@router.put("/{document_id}", response_model=DocumentI)
def update_document(document_id: int, document: DocumentBase, db: Session = Depends(get_db)):
    db_document = DMSService.update_document(db=db, document_id=document_id, document=document)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document

@router.delete("/{document_id}", response_model=DocumentI)
def delete_document(document_id: int, db: Session = Depends(get_db)):
    db_document = DMSService.delete_document(db=db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document

# @router.post("/attach_documents/{employee_id}", response_model=List[Document])
# def attach_documents_to_employee(employee_id: int, documents: List[DocumentCreate], db: Session = Depends(get_db)):
#     attached_documents = DMSService.attach_documents_to_employee(db=db, employee_id=employee_id, documents_data=documents)
#     if not attached_documents:
#         raise HTTPException(status_code=404, detail="Employee not found or no documents attached")
#     return attached_documents


# @router.post("/attach_documents/{employee_id}", response_model=List[Document])
# async def attach_documents_to_employee(employee_id: int, files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
#     attached_documents = []
#     for document_file in files:
#         # Save the file to a specified directory
#         file_path = save_uploaded_file(document_file)

#         # Create the document in the database
#         document = Document(file_path=file_path, created_by=employee_id)
#         db.add(document)
#         db.commit()
#         db.refresh(document)
#         attached_documents.append(document)
#     return attached_documents
class DocumentMetadata(BaseModel):
    title: str
    description: Optional[str]
    category_id: Optional[int]

@router.post("/attach_documents/{employees_id}")
async def attach_documents_to_employee(
    employees_id: int,
    files: List[UploadFile] = File(...),
    metadata_json: str = Form(...),
    db: Session = Depends(get_db)
):
    metadata = json.loads(metadata_json)
    if len(files) != len(metadata):
        raise HTTPException(status_code=400, detail="The number of files and metadata entries must match")

    attached_documents = []
    for file, data in zip(files, metadata):
        file_path = await save_uploaded_file(file)
        document = Document(
            title=data["title"],
            description=data.get("description"),
            file_path=file_path,
            employee_id=employees_id,
            category_id=data.get("category_id"),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.add(document)
        db.commit()
        db.refresh(document)
        attached_documents.append(document)
    
    return attached_documents
async def save_uploaded_file(file: UploadFile) -> str:
    upload_dir = Path("uploads")
    if not upload_dir.exists():
        upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = upload_dir / file.filename
    async with aiofiles.open(file_path, 'wb') as buffer:
        await buffer.write(await file.read())
    return str(file_path)


@router.get("/download/{filename}")
async def download_file(filename: str):
    upload_dir = Path("uploads")  # Ensure this is the same directory as used in save_uploaded_file function
    file_path = upload_dir / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=file_path, filename=filename, media_type='application/octet-stream')


@router.get("/download_all/{employees_id}")
async def download_all_files(employees_id: int, db: Session = Depends(get_db)):
    # Query the database to get all documents for the employee
    documents = db.query(Document).filter(Document.employee_id == employees_id).all()

    if not documents:
        raise HTTPException(status_code=404, detail="No documents found for the employee")

    # Create a temporary zip file
    with NamedTemporaryFile(delete=False) as tmp_file:
        with zipfile.ZipFile(tmp_file, 'w') as zipf:
            for document in documents:
                file_path = Path(document.file_path)
                if file_path.exists():
                    zipf.write(file_path, arcname=file_path.name)
        
        tmp_file_path = tmp_file.name

    return FileResponse(path=tmp_file_path, filename=f"employee_{employees_id}_documents.zip", media_type='application/zip')


# @router.get("/download_file/{documents_id}")
# async def download_file(documents_id: int, db: Session = Depends(get_db)):
#     # Query the database to get the document
#     document = db.query(Document).filter(Document.document_id == documents_id).first()

#     # If the document does not exist in the database, raise a 404 error
#     if not document:
#         raise HTTPException(status_code=404, detail="Document not found")

#     # Get the file path from the document
#     file_path = Path(document.file_path)

#     # If the file does not exist at the specified path, raise a 404 error
#     if not file_path.exists():
#         raise HTTPException(status_code=404, detail="File not found on the server")

#     # Return the file as a response
#     return FileResponse(path=file_path, filename=file_path.name, media_type='application/octet-stream')

import mimetypes

@router.get("/download_file/{document_id}")
async def download_file(document_id: int, db: Session = Depends(get_db)):
    # Query the database to get the document
    document = db.query(Document).filter(Document.document_id == document_id).first()

    # If the document does not exist in the database, raise a 404 error
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    # Get the file path from the document
    file_path = Path(document.file_path)

    # If the file does not exist at the specified path, raise a 404 error
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found on the server")

    # Determine the media type based on the file extension
    media_type = mimetypes.guess_type(file_path.as_posix())[0] or "application/octet-stream"

    # Return the file as a response with the correct media type
    return FileResponse(path=file_path, filename=file_path.name, media_type=media_type)


@router.get("/api/employees/{employee_id}/documents", response_model=List[DocumentOut])
async def get_employee_documents(employee_id: int, db: Session = Depends(get_db)):
    documents = db.query(Document).filter(Document.employee_id == employee_id).all()
    print(documents)  # Debugging line
    if not documents:
        raise HTTPException(status_code=404, detail="Documents not found for the given employee ID")
    return documents


@router.get("/employee_documents_by_title/{employees_id}")
async def get_employee_documents(employees_id: int, db: Session = Depends(get_db)):
    # Query the database to get all documents for the employee
    # documents = db.query(Document).filter(Document.created_by == employee_id).all()
    documents = db.query(Document).filter(Document.employee_id == employees_id).all()

    if not documents:
        raise HTTPException(status_code=404, detail="No documents found for the employee")

    # Construct the response
    document_list = [
        {
            "title": document.title,
            "download_url": f"/download/{Path(document.file_path).name}"
        }
        for document in documents
    ]

    return document_list

@router.get("/all-categories", response_model=List[DocumentCategorys])
def get_all_categories(db: Session = Depends(get_db)):
    return DMSService.get_all_categories(db)





@router.get("/api/titles", response_model=List[TitleResponse])
def get_titles_by_category(category_id: int, db: Session = Depends(get_db)):
    if category_id not in CATEGORY_TITLE_MAPPING:
        raise HTTPException(status_code=404, detail="No titles found for this category")
    
    titles = CATEGORY_TITLE_MAPPING[category_id]
    return [TitleResponse(title=title.value) for title in titles]

@router.get("/api/categories", response_model=List[DocumentCategorys])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(DocumentCategory).all()
    return categories
# @router.post("/upload/")
# async def upload_files(files: List[UploadFile] = File(...)):
#     file_names = []
#     for file in files:
#         contents = await file.read()
#         file_names.append(file.filename)
#         # Do something with the contents of the file
        
#     return JSONResponse(content={"uploaded_files": file_names})



@router.delete("/delete_document/{document_id}", response_model=DocumentI)
def delete_document(document_id: int, db: Session = Depends(get_db)):
    db_document = DMSService.delete_document(db=db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document
@router.get("/download/work_contract")
async def download_work_contract(request: Request):
    template_path = "./DMS/F-057 Kontrata e punes E-Tech.docx"
    
    # Debugging: Print the resolved path
    print(f"Resolved path: {os.path.abspath(template_path)}")

    if not os.path.exists(template_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    # Send the file as a response
    return FileResponse(template_path, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')