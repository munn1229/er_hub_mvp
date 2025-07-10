from pydantic import BaseModel, Field
from typing import Dict, Any

class CommitOut(BaseModel):
    id: int
    body: str

    class Config:
        orm_mode = True

