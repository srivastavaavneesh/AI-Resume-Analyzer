"""
Unit tests for ResumeService functionality.
"""

from unittest.mock import AsyncMock, patch

import pytest

from ai_resume_analyzer.services.resume_service import ResumeService


@pytest.mark.asyncio
async def test_extract_resume_text(create_upload_file):
    """
    Verify that extract_resume_text returns the expected text
    when the document extraction service successfully parses a PDF.
    """
    # Create a fake UploadFile representing a PDF
    file = create_upload_file(
        filename="resume.pdf",
        content=b"dummy",
        content_type="application/pdf",
    )

    service = ResumeService()

    # Patch the document extraction service to simulate successful text extraction
    with patch(
        "ai_resume_analyzer.services.resume_service.document_extraction_service.extract_text",
        new_callable=AsyncMock,
    ) as mock_extract:
        mock_extract.return_value = "John Doe Resume"

        result = await service.extract_resume_text(file)

        # The returned text should match the mocked output
        assert result == "John Doe Resume"
