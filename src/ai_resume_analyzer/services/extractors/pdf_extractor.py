"""
PDF document extractor.

Provides PDF text extraction using the PyPDF library.
"""

from io import BytesIO

from fastapi import UploadFile
from pypdf import PdfReader

from ai_resume_analyzer.exceptions.document import (
    CorruptedDocumentException,
    PasswordProtectedDocumentException,
)
from ai_resume_analyzer.services.extractors.base import BaseDocumentExtractor


class PdfExtractor(BaseDocumentExtractor):
    """
    Extracts text from PDF documents.
    """

    async def extract_text(self, file: UploadFile) -> str:
        """
        Extract text from a PDF document.

        Args:
            file: Uploaded PDF file.

        Returns:
            Extracted text from all PDF pages.
        """

        pdf_bytes = await file.read()

        reader = PdfReader(BytesIO(pdf_bytes))

        extracted_pages = []

        for page in reader.pages:
            page_text = page.extract_text() or ""
            extracted_pages.append(page_text)

        return "\n".join(extracted_pages)

    async def validate_document(self, file: UploadFile) -> None:
        """
        Validate the uploaded PDF document.

        Args:
            file: Uploaded PDF file.

        Raises:
            PasswordProtectedDocumentException:
                If the PDF is password protected.

            CorruptedDocumentException:
                If the PDF is corrupted or unreadable.
        """

        try:
            file.file.seek(0)

            reader = PdfReader(file.file)

            if reader.is_encrypted:
                raise PasswordProtectedDocumentException()

            # Try reading the first page
            if reader.pages:
                reader.pages[0]

        except PasswordProtectedDocumentException:
            raise

        except Exception as exc:
            raise CorruptedDocumentException() from exc

        finally:
            # Reset stream for extraction
            file.file.seek(0)
