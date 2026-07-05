"""
API route package.

Exports all application routers for the AI Resume Analyzer.
This module acts as a central entry point, collecting and exposing
individual route modules (health, resume) so they can be registered
with the FastAPI application.
"""

# Import individual routers from their respective modules
from ai_resume_analyzer.api.routes.health import router as health_router
from ai_resume_analyzer.api.routes.resume import router as resume_router

# __all__ defines the public API of this package.
# Only the listed routers will be exported when using:
#   from ai_resume_analyzer.api.routes import *
__all__ = [
    "health_router",  # Health check endpoint router
    "resume_router",  # Resume upload/analysis endpoint router
]
