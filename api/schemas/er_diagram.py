from pydantic import BaseModel, Field

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

    class Config:
        orm_mode = True
