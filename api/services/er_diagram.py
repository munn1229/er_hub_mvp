from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, selectinload
from db import get_db
from schemas import ErDiagramIn, ErDiagramCommitIn
from models import ErDiagram, Branch, Commit

async def store(payload: ErDiagramIn, db: AsyncSession):
    try:
        er_diagram = ErDiagram(
            project_id=payload.project_id,
            user_id=payload.user_id,
            name=payload.name
        )

        db.add(er_diagram)
        await db.flush()

        branch = Branch(
            er_diagram_id=er_diagram.id,
            user_id=payload.user_id,
            name="master"
        )
        db.add(branch)
        await db.flush()

        commit = Commit(
            branch_id=branch.id,
            user_id=payload.user_id,
            body={},
            comment="created by api"
        )
        db.add(commit)
        await db.commit()

        return er_diagram
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail="er_diagramsの作成に失敗しました。"
        )

async def update(id: int, payload: ErDiagramCommitIn, db:AsyncSession):
    try:
        result = await db.execute(select(ErDiagram).options(selectinload(ErDiagram.branches).selectinload(Branch.commits)).where(ErDiagram.id == id))
        er_diagram = result.scalar_one_or_none()
        if er_diagram is None:
            raise HTTPException(status_code=404, detail="ER図が見つかりません")
        
        commit = er_diagram.master_branch.latest_commit
        if commit is None:
            raise HTTPException(status_code = 404, detail="最新のコミットが見つかりません。")

        commit.body = payload.er_body

        await db.commit()
        
        return er_diagram
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail="er_diagramsの更新に失敗しました。"
        )
