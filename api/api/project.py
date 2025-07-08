from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from db import get_db
from models.project import Project

class ProjectIn(BaseModel):
    user_id: str = Field(
        ...,
    )
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

@router.get("/projects", response_model=list[ProjectOut])
async def index(
    user_id: int | None = Query(default=None),
    name: str | None = Query(default=None),
    db: Session = Depends(get_db)
):
    query = select(Project).where(Project.is_public == True)

    result = await db.execute(query)
    projects = result.scalars().all()
    return projects

@router.post("/projects")
async def store(payload: ProjectIn, db: Session = Depends(get_db)):
    new_project = Project(
        user_id=payload.user_id,
        name=payload.name,
        is_public=True
    )

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
