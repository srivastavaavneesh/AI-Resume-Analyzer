import pytest
from unittest.mock import AsyncMock, patch

from ai_resume_analyzer.services.resume_service import ResumeService


@pytest.mark.asyncio
async def test_extract_resume_text(create_upload_file):
    """
    Should return extracted resume text.
    """

    file = create_upload_file(
        filename="resume.pdf",
        content=b"dummy",
        content_type="application/pdf",
    )

    service = ResumeService()

    with patch(
        "ai_resume_analyzer.services.resume_service.document_extraction_service.extract_text",
        new_callable=AsyncMock,
    ) as mock_extract:

        mock_extract.return_value = "John Doe Resume"

        result = await service.extract_resume_text(file)

        assert result == "John Doe Resume"