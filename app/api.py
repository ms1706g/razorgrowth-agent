from fastapi import APIRouter, HTTPException

from app.agent import run_growth_agent
from app.tools import analyze_merchant, find_growth_opportunity

router = APIRouter()


@router.get("/")
def root():
    return {
        "name": "RazorGrowth",
        "description": "Agentic Merchant Growth Engine",
        "status": "running",
    }


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.get("/merchant/analyze")
def merchant_analysis():
    return analyze_merchant()


@router.get("/merchant/opportunity")
def growth_opportunity():
    return find_growth_opportunity()


@router.post("/agent/analyze")
def agent_analysis():
    try:
        return run_growth_agent()
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )