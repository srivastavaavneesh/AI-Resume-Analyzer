"""
Factory for creating AI providers.

Centralizes the creation of AI provider instances (Gemini, Groq, etc.).
Ensures consistent initialization of primary and fallback providers
based on application settings.
"""

from ai_resume_analyzer.ai.providers.gemini_provider import GeminiProvider
from ai_resume_analyzer.ai.providers.groq_provider import GroqProvider
from ai_resume_analyzer.core.config import settings


class ProviderFactory:
    """
    Factory class for creating AI providers.

    Responsibilities:
        - Instantiate provider classes based on provider name.
        - Support multiple provider implementations (Gemini, Groq).
        - Provide helper methods for creating primary and fallback providers
          as defined in application settings.

    Methods:
        create(provider_name: str) -> AIProvider:
            Create an AI provider instance based on the given name.

        create_primary() -> AIProvider:
            Create the primary provider defined in settings.

        create_fallback() -> AIProvider:
            Create the fallback provider defined in settings.
    """

    @staticmethod
    def create(provider_name: str):
        """
        Create an AI provider instance.

        Args:
            provider_name (str): Name of the provider ("gemini" or "groq").

        Returns:
            AIProvider: Instance of the requested provider.

        Raises:
            ValueError: If the provider name is unsupported.
        """
        if provider_name == "gemini":
            return GeminiProvider()

        if provider_name == "groq":
            return GroqProvider()

        raise ValueError(f"Unsupported AI Provider: {provider_name}")

    @staticmethod
    def create_primary():
        """
        Create the primary provider defined in settings.

        Returns:
            AIProvider: Primary provider instance.
        """
        return ProviderFactory.create(settings.primary_provider)

    @staticmethod
    def create_fallback():
        """
        Create the fallback provider defined in settings.

        Returns:
            AIProvider: Fallback provider instance.
        """
        return ProviderFactory.create(settings.fallback_provider)
