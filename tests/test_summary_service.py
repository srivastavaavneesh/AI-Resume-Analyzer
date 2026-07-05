"""
Unit tests for SummaryService functionality.
"""

from unittest.mock import Mock, patch

from ai_resume_analyzer.services.summary_service import SummaryService


@patch("ai_resume_analyzer.services.summary_service.ai_client")
def test_generate_summary(mock_ai_client):
    """
    Verify that generate_summary returns the expected text
    when the AI client successfully generates a professional summary.
    """
    service = SummaryService()

    mock_ai_client.generate_text.return_value = Mock(content="Professional summary")

    result = service.generate_summary("resume text")

    assert result == "Professional summary"


@patch("ai_resume_analyzer.services.summary_service.ai_client")
def test_generate_summary_empty(mock_ai_client):
    """
    Verify that generate_summary returns an empty string
    when the AI client generates no content.
    """
    service = SummaryService()

    mock_ai_client.generate_text.return_value = Mock(content="")

    result = service.generate_summary("resume text")

    assert result == ""
