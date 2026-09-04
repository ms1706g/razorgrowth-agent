from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import router
from app.database import initialize_database


app = FastAPI(
    title="RazorGrowth — Agentic Merchant Growth Engine",
    version="1.0.0",
    description="Agentic AI engine for merchant growth recommendations.",
)

initialize_database()

app.include_router(router)

app.mount("/dashboard", StaticFiles(directory="app/static", html=True), name="dashboard")