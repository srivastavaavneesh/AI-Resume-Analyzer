# -----------------------------------------------------------------------------
# File: main.py
# Purpose: Application entry point for AI Resume Analyzer.
#          Initializes FastAPI app, mounts static files, registers exception
#          handlers, and includes API/UI routers.
# -----------------------------------------------------------------------------

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from ai_resume_analyzer.api.routes import health_router, resume_router
from ai_resume_analyzer.core.config import settings
from ai_resume_analyzer.exceptions.handlers import register_exception_handlers
from ai_resume_analyzer.ui.routes import router as ui_router

# Initialize FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="AI-powered resume analysis platform built with FastAPI.",
    version=settings.app_version,
)

# Mount static files
app.mount(
    "/static",
    StaticFiles(directory="src/ai_resume_analyzer/static"),
    name="static",
)

# Register exception handlers
register_exception_handlers(app)

# Register UI routers
app.include_router(ui_router)

# Register API routers
app.include_router(resume_router)
app.include_router(health_router)
