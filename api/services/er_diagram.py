from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from db import get_db
from schemas import ErDiagramIn
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
