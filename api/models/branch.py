from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from .base import Base

class Branch(Base):
    __tablename__ = "branches"
    id = Column(Integer, primary_key=True, index=True)
    er_diagram_id = Column(Integer, ForeignKey("er_diagrams.id"), index=True, nullable=False)
    
    user_id = Column(CHAR(36, collation='utf8mb4_unicode_ci'), ForeignKey("users.id"), index=True, nullable=False)

    name = Column(String(20), index=True, nullable=False)
    
