from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from .branch import BranchOut

class ErDiagramIn(BaseModel):
    user_id: str = Field(
        ...,
    )
    project_id: int = Field(
        ...,
    )
    name: str = Field(
        ...,
        max_length=20
    )

class ErDiagramOut(BaseModel):
    id: int
    name: str
    master_branch: Optional[BranchOut]

    class Config:
        orm_mode = True

class ErDiagramCommitIn(BaseModel):
    er_body: dict
