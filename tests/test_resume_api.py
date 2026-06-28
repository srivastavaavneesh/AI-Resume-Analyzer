import pytest
from unittest.mock import AsyncMock, patch


def test_extract_resume_endpoint(client):
    """
    Should return extracted resume text.
    """

    with patch(
        "ai_resume_analyzer.api.routes.resume.resume_service.extract_resume_text",
        new_callable=AsyncMock,
    ) as mock_extract:

        mock_extract.return_value = "John Doe Resume"

        response = client.post(
            "/resume/upload",
            files={
                "file": (
                    "resume.pdf",
                    b"dummy pdf",
                    "application/pdf",
                )
            },
        )

        assert response.status_code == 200
        assert response.json()["message"] == "Resume processed successfully."
        assert response.json()["extracted_text"] == "John Doe Resume"