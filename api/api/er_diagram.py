from fastapi import APIRouter, HTTPException, Depends, Query, Path
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, selectinload
from db import get_db
from models.er_diagram import ErDiagram
from models.branch import Branch
from models.commit import Commit
from schemas import ErDiagramIn, ErDiagramOut, ErDiagramCommitIn
from services.er_diagram import store as er_diagram_store
from services.er_diagram import update as er_diagram_update

router = APIRouter()

@router.get("/er_diagrams", response_model=list[ErDiagramOut])
async def index(
    user_id: int | None = Query(default=None),
    project_id: int | None = Query(default=None),
    name: str | None = Query(default=None),
    db: Session = Depends(get_db)
):
    query = select(ErDiagram).options(selectinload(ErDiagram.branches).selectinload(Branch.commits))

    if project_id is not None:
        query = query.where(ErDiagram.project_id == project_id)

    result = await db.execute(query)
    er_diagrams = result.scalars().all()
    return er_diagrams

@router.get("/er_diagrams/{id}", response_model=ErDiagramOut)
async def show(
    id: int = Path(...),
    db: Session = Depends(get_db)
):
    try:
        result = await db.execute(select(ErDiagram).options(selectinload(ErDiagram.branches).selectinload(Branch.commits)).where(ErDiagram.id == id))
        er_diagram = result.scalar_one_or_none()
        if er_diagram is None:
            raise HTTPException(status_code=404, detail="ER図が見つかりません")
        return er_diagram
    except SQLAlchemyError as e:
        print(e._message)
        raise HTTPException(status_code=500, detail="ER図の取得中にエラーが発生しました。")

@router.post("/er_diagrams")
async def store(payload: ErDiagramIn, db: Session = Depends(get_db)):
    return await er_diagram_store(payload, db)

@router.patch("/er_diagrams/{id}")
async def update(payload: ErDiagramCommitIn, id: int = Path(...), db: Session = Depends(get_db)):
    return await er_diagram_update(id, payload, db)

