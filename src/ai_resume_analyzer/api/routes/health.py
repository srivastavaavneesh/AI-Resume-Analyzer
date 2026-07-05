"""
Health check API routes.

Provides system status endpoints for monitoring and deployment validation.
Useful for load balancers, uptime monitoring, and CI/CD pipelines to verify
that the application is running correctly.
"""

from fastapi import APIRouter

from ai_resume_analyzer.core.config import settings

# Create a router instance with a "Health" tag
# This groups the endpoint under "Health" in API docs.
router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check():
    """
    Health Check Endpoint

    Purpose:
        - Returns application health status.
        - Used by monitoring tools and deployment scripts to validate service availability.

    Response:
        {
            "status_code": "200",       # HTTP-like status indicator
            "status": "healthy",        # Application health state
            "app": <application name>,  # From settings.app_name
            "version": <app version>    # From settings.app_version
        }
    """
    return {
        "status_code": "200",
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
    }
