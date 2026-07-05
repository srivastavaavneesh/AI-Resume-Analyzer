"""
Unit tests for ResumeLLMParserService functionality.
"""

from unittest.mock import Mock, patch

from ai_resume_analyzer.schemas.resume import ResumeData
from ai_resume_analyzer.services.llm_parser_service import ResumeLLMParserService


@patch("ai_resume_analyzer.services.llm_parser_service.ai_client")
def test_parse_success(mock_ai_client):
    """
    Verify that parse returns a ResumeData instance when the AI client
    successfully generates valid JSON output.
    """
    service = ResumeLLMParserService()

    mock_ai_client.generate_text.return_value = Mock(
        content="""
        {
            "extracted_text": "resume",
            "name": "John",
            "email": "john@test.com",
            "phone": "9999999999",
            "linkedin": null,
            "github": null,
            "skills": [],
            "experience": [],
            "education": [],
            "projects": [],
            "certifications": [],
            "summary": null
        }
        """
    )

    result = service.parse("resume")

    assert isinstance(result, ResumeData)
    assert result.name == "John"


@patch("ai_resume_analyzer.services.llm_parser_service.parser_service")
@patch("ai_resume_analyzer.services.llm_parser_service.ai_client")
def test_parse_fallback(mock_ai_client, mock_parser):
    """
    Verify that parse falls back to parser_service when the AI client
    raises an exception during text generation.
    """
    service = ResumeLLMParserService()

    mock_ai_client.generate_text.side_effect = Exception("AI Failed")

    fallback = ResumeData(extracted_text="resume")
    mock_parser.parse.return_value = fallback

    result = service.parse("resume")

    assert result == fallback


@patch("ai_resume_analyzer.services.llm_parser_service.parser_service")
@patch("ai_resume_analyzer.services.llm_parser_service.ai_client")
def test_invalid_json_fallback(mock_ai_client, mock_parser):
    """
    Verify that parse falls back to parser_service when the AI client
    returns invalid JSON output.
    """
    service = ResumeLLMParserService()

    mock_ai_client.generate_text.return_value = Mock(content="INVALID JSON")

    fallback = ResumeData(extracted_text="resume")
    mock_parser.parse.return_value = fallback

    result = service.parse("resume")

    assert result == fallback
