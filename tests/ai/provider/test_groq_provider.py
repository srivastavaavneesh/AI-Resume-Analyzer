"""
Unit tests for GroqProvider health check functionality.
"""

from unittest.mock import patch

from ai_resume_analyzer.ai.providers.groq_provider import GroqProvider


@patch(
    "ai_resume_analyzer.ai.providers.groq_provider.settings.groq_api_key", "dummy-key"
)
@patch("ai_resume_analyzer.ai.providers.groq_provider.Groq")
def test_health_check_success(mock_groq):
    mock_groq.return_value.chat.completions.create.return_value = {}

    provider = GroqProvider()

    assert provider.health_check() is True


@patch("ai_resume_analyzer.ai.providers.groq_provider.Groq")
def test_health_check_failure(mock_groq):
    """
    Verify that health_check returns False when the Groq client
    raises an exception during chat.completions.create().
    """
    mock_groq.return_value.chat.completions.create.side_effect = Exception()

    provider = GroqProvider()

    assert provider.health_check() is False
