"""
API route package.

Exports all application routers.
"""

from ai_resume_analyzer.api.routes.health import router as health_router
from ai_resume_analyzer.api.routes.resume import router as resume_router

__all__ = [
    "health_router",
    "resume_router",
]