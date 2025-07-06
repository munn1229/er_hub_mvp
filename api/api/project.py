from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from db import get_db
from models.project import Project

class ProjectIn(BaseModel):
    name: str = Field(
        ...,
        max_length=20
    )

class ProjectOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

router = APIRouter()

@router.post("/projects")
async def store(payload: ProjectIn, db: Session = Depends(get_db)):
    new_project = Project(
        user_id=1,
        name=payload.name,
        is_public=True
    )

    print('test')

    try:
        db.add(new_project)
        await db.commit()
        await db.refresh(new_project)
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail="projectsの作成に失敗しました。"
        )

    return new_project
