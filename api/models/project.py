from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(36), index=True, nullable=False)
    name = Column(String(20), index=True, nullable=False)
    is_public = Column(Boolean, default=True, nullable=False)
    
