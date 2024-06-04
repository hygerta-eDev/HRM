from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from fastapi import UploadFile

class DocumentBase(BaseModel):
    title: str
    description: Optional[str] = None
    file_path: str
    category_id: Optional[int] = None

class DocumentCreate(DocumentBase):
    # created_by: int
    pass

class DocumentI(DocumentBase):
    document_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
class Documentss(BaseModel):
    title: str
    # document_id: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    file_path: str
    created_by: int

class DocumentVersionBase(BaseModel):
    document_id: int
    version_number: int
    file_path: str

class DocumentVersionCreate(DocumentVersionBase):
    created_by: int

class DocumentVersion(DocumentVersionBase):
    version_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class DocumentCategoryBase(BaseModel):
    category_name: str
    description: Optional[str] = None

class DocumentCategoryCreate(DocumentCategoryBase):
    pass

class DocumentCategory(DocumentCategoryBase):
    category_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class DocumentAccessBase(BaseModel):
    document_id: int
    employee_id: int
    access_level: str

class DocumentAccessCreate(DocumentAccessBase):
    granted_by: int

class DocumentAccess(DocumentAccessBase):
    access_id: int
    granted_at: datetime

    class Config:
        orm_mode = True

class DocumentAuditBase(BaseModel):
    document_id: int
    employee_id: int
    action: str

class DocumentAuditCreate(DocumentAuditBase):
    pass

class DocumentAudit(DocumentAuditBase):
    audit_id: int
    action_timestamp: datetime

    class Config:
        orm_mode = True

class DocumentTagBase(BaseModel):
    tag_name: str

class DocumentTagCreate(DocumentTagBase):
    pass

class DocumentTag(DocumentTagBase):
    tag_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class DocumentTagMapBase(BaseModel):
    document_id: int
    tag_id: int

class DocumentTagMapCreate(DocumentTagMapBase):
    pass

class DocumentTagMap(DocumentTagMapBase):
    pass

    class Config:
        orm_mode = True


class DocumentCategorys(BaseModel):
    category_id: int
    category_name: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class FileUpload(BaseModel):
    files: List[UploadFile]