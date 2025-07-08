from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from db import get_db
from models.er_diagram import ErDiagram
from models.branch import Branch
from models.commit import Commit
from schemas import ErDiagramIn, ErDiagramOut
from services.er_diagram import store as er_diagram_store

router = APIRouter()

@router.get("/er_diagrams", response_model=list[ErDiagramOut])
async def index(
    user_id: int | None = Query(default=None),
    project_id: int | None = Query(default=None),
    name: str | None = Query(default=None),
    db: Session = Depends(get_db)
):
    query = select(ErDiagram)

    if project_id is not None:
        query = query.where(ErDiagram.project_id == project_id)

    result = await db.execute(query)
    er_diagrams = result.scalars().all()
    return er_diagrams

@router.post("/er_diagrams")
async def store(payload: ErDiagramIn, db: Session = Depends(get_db)):
    return await er_diagram_store(payload, db)

