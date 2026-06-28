"""
Base document extractor.

Defines the contract that all document extractors must implement.
"""

from abc import ABC, abstractmethod

from fastapi import UploadFile


class BaseDocumentExtractor(ABC):
    """
    Abstract base class for all document extractors.
    """

    @abstractmethod
    async def validate_document(self, file: UploadFile) -> None:
        """
        Validate that the uploaded document is readable and not corrupted.

        Raises:
            CorruptedFileException
        """
        pass
    
    @abstractmethod
    async def extract_text(self, file: UploadFile) -> str:
        """
        Extract text from the uploaded document.

        Args:
            file: Uploaded document.

        Returns:
            Extracted text.
        """
        pass   
    