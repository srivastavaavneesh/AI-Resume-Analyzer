"""
Unit tests for PdfExtractor functionality.
"""

from unittest.mock import MagicMock, patch

import pytest

from ai_resume_analyzer.exceptions import PasswordProtectedDocumentException
from ai_resume_analyzer.services.extractors import PdfExtractor


@pytest.mark.asyncio
async def test_password_protected_pdf(create_upload_file):
    """
    Verify that validate_document raises PasswordProtectedDocumentException
    when the PDF file is encrypted (password-protected).
    """
    file = create_upload_file(
        filename="resume.pdf",
        content=b"dummy",
        content_type="application/pdf",
    )

    extractor = PdfExtractor()

    # Patch PdfReader to simulate an encrypted PDF
    with patch(
        "ai_resume_analyzer.services.extractors.pdf_extractor.PdfReader"
    ) as mock_reader:
        mock_pdf = MagicMock()
        mock_pdf.is_encrypted = True
        mock_reader.return_value = mock_pdf

        with pytest.raises(PasswordProtectedDocumentException):
            await extractor.validate_document(file)


@pytest.mark.asyncio
async def test_extract_text_success(create_upload_file):
    """
    Verify that extract_text successfully returns text
    when the PDF contains at least one page with extractable content.
    """
    file = create_upload_file(
        filename="resume.pdf",
        content=b"dummy",
        content_type="application/pdf",
    )

    extractor = PdfExtractor()

    # Patch PdfReader to simulate a PDF with one page containing text
    with patch(
        "ai_resume_analyzer.services.extractors.pdf_extractor.PdfReader"
    ) as mock_reader:
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "Hello World"

        mock_pdf = MagicMock()
        mock_pdf.pages = [mock_page]
        mock_reader.return_value = mock_pdf

        result = await extractor.extract_text(file)

        assert result == "Hello World"
