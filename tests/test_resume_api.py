"""
Unit tests for the /resume/upload endpoint.
"""

from unittest.mock import AsyncMock, patch


def test_extract_resume_endpoint(client):
    """
    Verify that the /resume/upload endpoint processes a PDF file
    and returns the expected extracted resume text.
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
                    "resume.pdf",  # filename
                    b"dummy pdf",  # file content
                    "application/pdf",  # MIME type
                )
            },
        )

        # Endpoint should respond with HTTP 200
        assert response.status_code == 200

        body = response.json()

        # Response body should confirm success and include extracted text
        assert body["message"] == "Resume processed successfully."
        assert body["extracted_text"] == "John Doe Resume"
