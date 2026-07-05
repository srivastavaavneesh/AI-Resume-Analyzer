from ai_resume_analyzer.ai.client import ai_client
from ai_resume_analyzer.core.logging.logger import get_logger
from ai_resume_analyzer.prompts.summary_prompt import SUMMARY_PROMPT

logger = get_logger(__name__)


class SummaryService:
    """
    Generates professional resume summaries.
    """

    def generate_summary(
        self,
        resume_text: str,
    ) -> str:
        logger.info("Generating resume summary")
        response = ai_client.generate_text(
            prompt=SUMMARY_PROMPT,
            context=resume_text,
        )
        logger.info("Resume summary generated")
        return response.content


summary_service = SummaryService()
