"""
Unit tests for ResponseParser functionality.
"""

from types import SimpleNamespace

import pytest

from ai_resume_analyzer.ai.exceptions import InvalidResponseError
from ai_resume_analyzer.ai.response_parser import ResponseParser


def test_extract_text_success():
    """
    Verify that extract_text returns the expected string
    when the response object contains valid text.
    """
    response = SimpleNamespace(text="Hello")

    assert ResponseParser.extract_text(response) == "Hello"


def test_extract_text_empty():
    """
    Verify that extract_text raises InvalidResponseError
    when the response object contains an empty text value.
    """
    response = SimpleNamespace(text="")

    with pytest.raises(InvalidResponseError):
        ResponseParser.extract_text(response)


def test_extract_text_missing():
    """
    Verify that extract_text raises InvalidResponseError
    when the response object does not contain a text attribute.
    """
    response = SimpleNamespace()

    with pytest.raises(InvalidResponseError):
        ResponseParser.extract_text(response)
