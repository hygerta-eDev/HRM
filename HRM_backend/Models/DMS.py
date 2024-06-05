from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from Config.database import Base
from .employeeModel import Employees

class Document(Base): 
    __tablename__ = 'documents'
    
    document_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    file_path = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('document_categories.category_id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
    category = relationship("DocumentCategory")
    employee = relationship("Employees", back_populates="documents")
    versions = relationship("DocumentVersion", back_populates="document")
    access_records = relationship("DocumentAccess", back_populates="document")
    audits = relationship("DocumentAudit", back_populates="document")

class DocumentVersion(Base):
    __tablename__ = 'document_versions'
    
    version_id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey('documents.document_id'), nullable=False)
    version_number = Column(Integer, nullable=False)
    file_path = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey('employees.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    document = relationship("Document", back_populates="versions")
    creator = relationship("Employees", back_populates="document_versions")

class DocumentCategory(Base):
    __tablename__ = 'document_categories'
    
    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, nullable=False, unique=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class DocumentAccess(Base):
    __tablename__ = 'document_access'
    
    access_id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey('documents.document_id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    access_level = Column(String, nullable=False)
    granted_by = Column(Integer, ForeignKey('employees.id'), nullable=False)
    granted_at = Column(DateTime, default=datetime.utcnow)
    
    document = relationship("Document", back_populates="access_records")
    employee = relationship("Employees", back_populates="document_access", foreign_keys=[employee_id])
    granter = relationship("Employees", back_populates="granted_access", foreign_keys=[granted_by])

class DocumentAudit(Base):
    __tablename__ = 'document_audit'
    
    audit_id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey('documents.document_id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    action = Column(String, nullable=False)
    action_timestamp = Column(DateTime, default=datetime.utcnow)
    
    document = relationship("Document", back_populates="audits")
    employee = relationship("Employees", back_populates="document_audits", foreign_keys=[employee_id])

class DocumentTag(Base):
    __tablename__ = 'document_tags'
    
    tag_id = Column(Integer, primary_key=True, index=True)
    tag_name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class DocumentTagMap(Base):
    __tablename__ = 'document_tag_map'
    
    document_id = Column(Integer, ForeignKey('documents.document_id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('document_tags.tag_id'), primary_key=True)

    document = relationship("Document")
    tag = relationship("DocumentTag")