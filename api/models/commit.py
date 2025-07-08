from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.dialects.mysql import CHAR, JSON
from .base import Base

class Commit(Base):
    __tablename__ = "commits"
    id = Column(Integer, primary_key=True, index=True)
    branch_id = Column(Integer, ForeignKey("branches.id"), index=True, nullable=False)
    
    user_id = Column(CHAR(36, collation='utf8mb4_unicode_ci'), ForeignKey("users.id"), index=True, nullable=False)

    body = Column(JSON, nullable=False)
    comment = Column(Text(collation='utf8mb4_unicode_ci'))

