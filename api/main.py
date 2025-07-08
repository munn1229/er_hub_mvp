from fastapi import FastAPI
from api.project import router as project_router
from api.er_diagram import router as er_diagram_router

app = FastAPI(title="erhub-api", version="0.1.0")

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(project_router)
app.include_router(er_diagram_router)
