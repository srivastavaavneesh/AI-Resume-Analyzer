"""
Document extraction service.

Delegates document text extraction to the appropriate extractor.
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
    """

    def __init__(self) -> None:
        """
        Initialize the extractor registry.
        """
        self._extractors: dict[str, BaseDocumentExtractor] = {
            ContentType.PDF: PdfExtractor(),
            ContentType.DOCX: DocxExtractor(),
        }

    async def extract_text(self, file: UploadFile) -> str:
        """
        Extract text from the uploaded document.

        Args:
            file: Uploaded document.

        Returns:
            Extracted document text.

        Raises:
            RuntimeError: If no extractor is registered for the document type.
        """

        extractor = self._extractors.get(file.content_type)

        if extractor is None:
            raise RuntimeError(
                f"No extractor registered for content type: {file.content_type}"
            )

        await extractor.validate_document(file)
        return await extractor.extract_text(file)


document_extraction_service = DocumentExtractionService()
