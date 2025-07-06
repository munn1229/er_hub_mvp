import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

dialect = os.getenv("DB_DIALECT", "mysql+aiomysql")
user = os.getenv("DB_USERNAME", "")
password = os.getenv("DB_PASSWORD", "")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "3306")
dbname = os.getenv("DB_DATABASE", "er_hub")

DATABASE_URL = f"{dialect}://{user}:{password}@{host}:{port}/{dbname}"
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
