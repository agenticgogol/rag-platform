# app/api/health.py

from fastapi import APIRouter
from app.schemas.response import HealthResponse
from app.core.config import settings

health_router = APIRouter(tags=["Health"])


@health_router.get("/health", response_model=HealthResponse)
def health():
    """
    Basic health endpoint for uptime checks.
    """
    return HealthResponse(status="healthy")


@health_router.get("/ready")
def readiness():
    """
    Readiness probe for Kubernetes.
    Add DB / Qdrant checks later if needed.
    """
    return {
        "status": "ready",
        "app": settings.APP_NAME,
        "env": settings.APP_ENV
    }


@health_router.get("/live")
def liveness():
    """
    Liveness probe for Kubernetes restart checks.
    """
    return {"status": "alive"}