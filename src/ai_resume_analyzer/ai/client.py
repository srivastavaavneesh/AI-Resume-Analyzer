"""
AI Client.

Main entry point for interacting with AI providers (Gemini, Groq, etc.).
Handles provider initialization, fallback logic, and unified access
to text and JSON generation methods.
"""

from groq import AuthenticationError
from openai import RateLimitError

from ai_resume_analyzer.ai.exceptions import ProviderUnavailableError
from ai_resume_analyzer.ai.provider_factory import ProviderFactory
from ai_resume_analyzer.core.config import settings
from ai_resume_analyzer.core.logging.logger import get_logger

logger = get_logger(__name__)


class AIClient:
    """
    Main entry point for AI providers.

    Responsibilities:
        - Initialize primary and fallback AI providers.
        - Route text and JSON generation requests to providers.
        - Handle provider failures gracefully with fallback logic.
        - Perform health checks across providers.

    Attributes:
        primary (AIProvider): Primary AI provider instance.
        fallback (AIProvider): Fallback AI provider instance.
    """

    def __init__(self):
        logger.info("Initializing AI Client...")
        self.primary = ProviderFactory.create_primary()
        self.fallback = ProviderFactory.create_fallback()

    def generate_text(self, prompt: str, context: str):
        """
        Generate text using the primary provider, with fallback if needed.

        Args:
            prompt (str): Input prompt for the AI provider.
            context (str): Additional context to guide the response.

        Returns:
            AIResponse: Structured response containing generated text.
        """
        try:
            logger.info("Using primary provider: %s", settings.primary_provider)
            return self.primary.generate_text(prompt, context)
        except Exception as ex:
            logger.warning("Primary provider failed: %s", ex)
            logger.info(
                "Switching to fallback provider: %s", settings.fallback_provider
            )
            return self.fallback.generate_text(prompt, context)

    def generate_json(self, prompt: str, context: str):
        """
        Generate JSON using the primary provider, with fallback if needed.

        Args:
            prompt (str): Input prompt for the AI provider.
            context (str): Additional context to guide the response.

        Returns:
            AIResponse: Structured response containing generated JSON.
        """
        try:
            return self.primary.generate_json(prompt, context)
        except (AuthenticationError, RateLimitError, ProviderUnavailableError):
            return self.fallback.generate_json(prompt, context)

    def health_check(self) -> bool:
        """
        Perform health checks on providers.

        Returns:
            bool: True if either primary or fallback provider is available.
        """
        return self.primary.health_check() or self.fallback.health_check()


# Singleton instance for reuse across the application
ai_client = AIClient()
