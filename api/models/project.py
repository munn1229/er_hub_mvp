from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from .base import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(CHAR(36, collation='utf8mb4_unicode_ci'), ForeignKey("users.id"), index=True, nullable=False)

    name = Column(String(20), index=True, nullable=False)
    is_public = Column(Boolean, default=True, nullable=False)
    
