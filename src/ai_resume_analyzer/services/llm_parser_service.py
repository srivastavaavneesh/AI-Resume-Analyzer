from json import JSONDecodeError

from pydantic import ValidationError

from ai_resume_analyzer.ai.client import ai_client
from ai_resume_analyzer.ai.json_parser import JsonParser
from ai_resume_analyzer.core.logging.logger import get_logger
from ai_resume_analyzer.prompts.parser_prompt import PARSER_PROMPT
from ai_resume_analyzer.schemas.resume import ResumeData
from ai_resume_analyzer.services.parser_service import parser_service

logger = get_logger(__name__)


class ResumeLLMParserService:
    """
    Uses AI to parse resumes with automatic fallback
    to the rule-based parser.
    """

    def parse(
        self,
        resume_text: str,
    ) -> ResumeData:
        try:
            logger.info("Parsing resume using AI")
            response = ai_client.generate_text(
                prompt=PARSER_PROMPT,
                context=resume_text,
            )

            data = JsonParser.loads(response.content)

            logger.info("Resume parsed successfully using AI")
            return ResumeData.model_validate(data)

        except (
            JSONDecodeError,
            ValidationError,
            Exception,
        ):
            logger.warning("AI parsing failed. Falling back to rule-based parser.")

            return parser_service.parse(resume_text)


llm_parser_service = ResumeLLMParserService()
