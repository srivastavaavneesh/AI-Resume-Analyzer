"""
Resume API routes.

Provides endpoints for uploading resumes and extracting text content.
This module acts as the interface between the frontend and the resume
extraction service, returning structured responses for further analysis.
"""

from fastapi import APIRouter, File, UploadFile

from ai_resume_analyzer.schemas.resume import ResumeExtractionResponse
from ai_resume_analyzer.services.resume_service import resume_service

# Create a router instance with a prefix and tag
# Prefix ensures all endpoints are under /resume
# Tag groups them in API docs
router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post(
    "/upload",
    response_model=ResumeExtractionResponse,
)
async def upload_resume(file: UploadFile = File(...)) -> ResumeExtractionResponse:
    """
    Upload Resume Endpoint

    Purpose:
        Accepts a resume file (PDF/DOCX) and extracts its text content
        for downstream processing such as ATS scoring, skill extraction,
        and interview insights.

    Args:
        file (UploadFile): The uploaded resume file provided by the user.

    Returns:
        ResumeExtractionResponse: A structured response containing:
            - message: Confirmation message
            - extracted_text: Raw text extracted from the resume
    """

    # Call the resume service to extract text from the uploaded file
    extracted_text = await resume_service.extract_resume_text(file)

    # Return structured response with extracted text
    return ResumeExtractionResponse(
        message="Resume processed successfully.",
        extracted_text=extracted_text,
    )
