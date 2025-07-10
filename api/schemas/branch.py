from pydantic import BaseModel, Field
from typing import Optional
from .commit import CommitOut

class BranchOut(BaseModel):
    id: int
    name: str
    latest_commit: Optional[CommitOut]

    class Config:
        orm_mode = True

