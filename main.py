from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.settings import settings

app = FastAPI(title="SD FF AI Esports Analyzer API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=settings.frontend_origins, allow_credentials=False, allow_methods=["GET", "POST"], allow_headers=["Content-Type", "Authorization"])
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"name": "SD FF AI Esports Analyzer", "status": "online", "docs": "/docs"}
