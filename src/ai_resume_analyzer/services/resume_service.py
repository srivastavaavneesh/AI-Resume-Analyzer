"""
Resume service.

Contains business logic related to resume processing.
"""

from fastapi import UploadFile
from ai_resume_analyzer.services.document_extraction_service import (
    document_extraction_service,
)
from ai_resume_analyzer.core.file_validator import FileValidator


class ResumeService:
    """Service responsible for processing uploaded resumes.
    """
    async def extract_resume_text(self,file: UploadFile) -> str:
        """Extracts text from the uploaded resume file.
        Args:
            file (UploadFile): The uploaded resume file.
        Returns:
            str:  Extracted resume text.
        """
        FileValidator.validate(file)
        return await document_extraction_service.extract_text(file)
    
resume_service = ResumeService()