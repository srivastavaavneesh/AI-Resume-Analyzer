"""
Unit tests for GeminiProvider health check functionality.
"""

from unittest.mock import patch

from ai_resume_analyzer.ai.providers.gemini_provider import GeminiProvider


@patch("ai_resume_analyzer.ai.providers.gemini_provider.genai.Client")
def test_health_check_success(mock_client):
    """
    Verify that health_check returns True when the Gemini client
    successfully responds to models.list().
    """
    mock_client.return_value.models.list.return_value = []

    provider = GeminiProvider()

    assert provider.health_check() is True


@patch("ai_resume_analyzer.ai.providers.gemini_provider.genai.Client")
def test_health_check_failure(mock_client):
    """
    Verify that health_check returns False when the Gemini client
    raises an exception during models.list().
    """
    mock_client.return_value.models.list.side_effect = Exception()

    provider = GeminiProvider()

    assert provider.health_check() is False
