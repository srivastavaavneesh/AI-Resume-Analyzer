"""
Unit tests for AIClient functionality.
"""

from unittest.mock import Mock

from ai_resume_analyzer.ai.client import AIClient


def test_generate_text():
    """
    Verify that generate_text delegates to the primary provider
    and returns the expected response.
    """
    client = AIClient()
    client.primary = Mock()
    client.primary.generate_text.return_value = "OK"

    result = client.generate_text("prompt", "context")

    assert result == "OK"


def test_generate_json():
    """
    Verify that generate_json delegates to the primary provider
    and returns the expected structured response.
    """
    client = AIClient()
    client.primary = Mock()
    client.primary.generate_json.return_value = {"name": "John"}

    result = client.generate_json("prompt", "context")

    assert result == {"name": "John"}


def test_health_check():
    """
    Verify that health_check returns True when the primary provider
    reports availability.
    """
    client = AIClient()
    client.primary = Mock()
    client.primary.health_check.return_value = True

    assert client.health_check() is True
