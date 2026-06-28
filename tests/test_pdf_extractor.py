from io import BytesIO

import pytest
from fastapi import UploadFile
from unittest.mock import MagicMock, patch

from ai_resume_analyzer.services.extractors import PdfExtractor
from ai_resume_analyzer.exceptions import PasswordProtectedDocumentException


@pytest.mark.asyncio
async def test_password_protected_pdf(create_upload_file):
    """
    Should raise exception for encrypted PDF.
    """

    file = create_upload_file(
        filename="resume.pdf",
        content=b"dummy",
        content_type= "application/pdf",
    )

    extractor = PdfExtractor()
    
    with patch("ai_resume_analyzer.services.extractors.pdf_extractor.PdfReader") as mock_reader:
        mock_pdf=MagicMock()
        mock_pdf.is_encrypted =True
        mock_reader.return_value = mock_pdf

        with pytest.raises(PasswordProtectedDocumentException):
            await extractor.validate_document(file)
            
            
@pytest.mark.asyncio
async def test_extract_text_success(create_upload_file):
    """
    Should extract text from a valid PDF.
    """

    file = create_upload_file(
        filename="resume.pdf",
        content=b"dummy",
        content_type="application/pdf",
    )

    extractor = PdfExtractor()

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