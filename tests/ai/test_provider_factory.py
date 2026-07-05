"""
Unit tests for ProviderFactory functionality.
"""

import pytest

from ai_resume_analyzer.ai.provider_factory import ProviderFactory
from ai_resume_analyzer.ai.providers.gemini_provider import GeminiProvider
from ai_resume_analyzer.ai.providers.groq_provider import GroqProvider


def test_create_gemini():
    """
    Verify that ProviderFactory.create returns a GeminiProvider
    instance when 'gemini' is specified.
    """
    provider = ProviderFactory.create("gemini")
    assert isinstance(provider, GeminiProvider)


def test_create_groq():
    """
    Verify that ProviderFactory.create returns a GroqProvider
    instance when 'groq' is specified.
    """
    provider = ProviderFactory.create("groq")
    assert isinstance(provider, GroqProvider)


def test_invalid_provider():
    """
    Verify that ProviderFactory.create raises a ValueError
    when an unsupported provider name is specified.
    """
    with pytest.raises(ValueError):
        ProviderFactory.create("invalid")
