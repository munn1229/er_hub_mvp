from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from .base import Base

class ErDiagram(Base):
    __tablename__ = "er_diagrams"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), index=True, nullable=False)
    
    user_id = Column(CHAR(36, collation='utf8mb4_unicode_ci'), ForeignKey("users.id"), index=True, nullable=False)

    name = Column(String(20), index=True, nullable=False)

    @property
    def master_branch(self):
        return next((branch for branch in self.branches if branch.name == "master"), None)
