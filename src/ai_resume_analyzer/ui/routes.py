# -----------------------------------------------------------------------------
# File: ui_routes.py
# Purpose: Defines FastAPI routes for rendering HTML pages (UI) of the
#          AI Resume Analyzer application. Handles landing page, upload page,
#          and resume analysis workflow.
# -----------------------------------------------------------------------------

from fastapi import APIRouter, File, Request, UploadFile
from fastapi.templating import Jinja2Templates

from ai_resume_analyzer.services.ats_service import ats_service
from ai_resume_analyzer.services.parser_service import parser_service
from ai_resume_analyzer.services.resume_service import resume_service

router = APIRouter(tags=["UI"])
templates = Jinja2Templates(directory="src/ai_resume_analyzer/templates")


@router.get("/")
async def home(request: Request):
    """Render landing page."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"app_name": "AI Resume Analyzer"},
    )


@router.get("/resume/upload")
async def upload_page(request: Request):
    """Render upload page."""
    return templates.TemplateResponse(
        request=request,
        name="resume/upload.html",
        context={},
    )


@router.post("/resume/analyze")
async def analyze_resume(request: Request, file: UploadFile = File(...)):
    """Analyze uploaded resume and render results page."""

    # Extract text from uploaded resume
    extracted_text = await resume_service.extract_resume_text(file)

    # Parse resume content
    parsed_resume = parser_service.parse(extracted_text)

    # Calculate ATS score
    ats = ats_service.calculate_score(parsed_resume)

    # Render result page
    return templates.TemplateResponse(
        request=request,
        name="resume/result.html",
        context={
            "filename": file.filename,
            "resume": parsed_resume,
            "ats": ats,
        },
    )
