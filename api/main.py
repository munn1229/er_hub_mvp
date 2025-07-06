from fastapi import FastAPI
from api.project import router as project_router

app = FastAPI(title="erhub-api", version="0.1.0")

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(project_router)
