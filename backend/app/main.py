from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import analysis, upload, health

app = FastAPI(title="CTR Suppression Intelligence Engine")

# CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(upload.router)
app.include_router(analysis.router)
