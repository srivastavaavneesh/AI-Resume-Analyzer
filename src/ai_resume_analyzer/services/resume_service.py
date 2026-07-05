"""
Resume service.

Contains business logic related to resume processing.
Acts as the orchestrator between file validation and document extraction,
ensuring uploaded resumes are properly validated and parsed into text.
"""

from fastapi import UploadFile

from ai_resume_analyzer.core.file_validator import FileValidator
from ai_resume_analyzer.services.document_extraction_service import (
    document_extraction_service,
)


class ResumeService:
    """
    Service responsible for processing uploaded resumes.

    Responsibilities:
        - Validate uploaded resume files (format, size, type).
        - Delegate text extraction to the DocumentExtractionService.
        - Provide a clean interface for API routes to consume.
    """

    async def extract_resume_text(self, file: UploadFile) -> str:
        """
        Extract text from the uploaded resume file.

        Workflow:
            1. Validate the file using FileValidator.
            2. Pass the file to DocumentExtractionService for text extraction.
            3. Return the extracted text.

        Args:
            file (UploadFile): The uploaded resume file.

        Returns:
            str: Extracted resume text.

        Raises:
            ValueError: If the file fails validation.
            RuntimeError: If no extractor is available for the file type.
        """
        # Step 1: Validate file (checks type, size, etc.)
        FileValidator.validate(file)

        # Step 2: Extract text using appropriate extractor (PDF/DOCX)
        return await document_extraction_service.extract_text(file)


# Singleton instance for reuse across the application
resume_service = ResumeService()
