"""
Resume API routes.

"""

from fastapi import APIRouter, File, UploadFile

from ai_resume_analyzer.schemas.resume import ResumeExtractionResponse
from ai_resume_analyzer.services.resume_service import resume_service

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post(
    "/upload",
    response_model=ResumeExtractionResponse,
)
async def upload_resume(file: UploadFile = File(...)) -> ResumeExtractionResponse:
    """
    Upload a resume and extract its text.

    Args:
        file: Uploaded resume file.

    Returns:
         ResumeExtractionResponse containing the extracted text.
    """

    extracted_text = await resume_service.extract_resume_text(file)

    return ResumeExtractionResponse(
        message="Resume processed successfully.",
        extracted_text=extracted_text,
    )
