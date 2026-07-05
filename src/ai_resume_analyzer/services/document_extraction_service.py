"""
Document extraction service.

Delegates document text extraction to the appropriate extractor
based on the uploaded file's content type (PDF, DOCX, etc.).
Ensures separation of concerns by centralizing extractor selection
and validation logic.
"""

from fastapi import UploadFile

from ai_resume_analyzer.core.constants import ContentType
from ai_resume_analyzer.services.extractors import (
    BaseDocumentExtractor,
    DocxExtractor,
    PdfExtractor,
)


class DocumentExtractionService:
    """
    Service responsible for selecting the appropriate document extractor.

    Maintains a registry of supported content types mapped to their
    corresponding extractor implementations. Provides a unified interface
    for validating and extracting text from uploaded documents.
    """

    def __init__(self) -> None:
        """
        Initialize the extractor registry.

        Maps MIME content types to extractor instances.
        Currently supports:
            - application/pdf → PdfExtractor
            - application/vnd.openxmlformats-officedocument.wordprocessingml.document → DocxExtractor
        """
        self._extractors: dict[str, BaseDocumentExtractor] = {
            ContentType.PDF: PdfExtractor(),
            ContentType.DOCX: DocxExtractor(),
        }

    async def extract_text(self, file: UploadFile) -> str:
        """
        Extract text from the uploaded document.

        Args:
            file (UploadFile): The uploaded document file.

        Returns:
            str: Extracted document text.

        Raises:
            RuntimeError: If no extractor is registered for the given content type.
        """
        # Select extractor based on file content type
        extractor = self._extractors.get(file.content_type)

        if extractor is None:
            raise RuntimeError(
                f"No extractor registered for content type: {file.content_type}"
            )

        # Validate document (e.g., check encryption, format issues)
        await extractor.validate_document(file)

        # Extract and return text
        return await extractor.extract_text(file)


# Singleton instance for reuse across the application
document_extraction_service = DocumentExtractionService()
