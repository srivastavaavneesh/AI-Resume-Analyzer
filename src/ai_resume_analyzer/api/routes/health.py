"""
Health check API routes.

Provides system status endpoints for monitoring and deployment validation.
"""

from fastapi import APIRouter

from ai_resume_analyzer.core.config import settings

router = APIRouter(
    tags=["Health"]
)


@router.get("/health")
def health_check():
    """
    Returns application health status.
    """
    return {
        "status_code": "200",
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
    }