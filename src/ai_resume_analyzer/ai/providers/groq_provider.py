"""
Groq AI Provider.

Implements the AIProvider interface using Groq.
Handles text and JSON generation requests, provider health checks,
and exception translation into framework-specific errors.
"""

import time

from groq import Groq

from ai_resume_analyzer.ai.providers.base import AIProvider
from ai_resume_analyzer.core.config import settings
from ai_resume_analyzer.core.logging.logger import get_logger
from ai_resume_analyzer.schemas.ai import AIResponse

logger = get_logger(__name__)


class GroqProvider(AIProvider):
    """
    Groq implementation of AIProvider.

    Responsibilities:
        - Initialize Groq client with API key and model settings.
        - Generate text and JSON responses from prompts and context.
        - Perform health checks to verify provider availability.
        - Provide consistent AIResponse objects for downstream services.

    Attributes:
        client (Groq): Groq client instance.
        model (str): Groq model name configured in settings.
    """

    def __init__(self):
        self.model = settings.groq_model
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = Groq(api_key=settings.groq_api_key)
            logger.info(f"Groq Provider initialized ({self.model})")
        return self._client

    def generate_text(self, prompt: str, context: str) -> AIResponse:
        """
        Generate a text response using Groq.

        Args:
            prompt (str): Input prompt for the AI provider.
            context (str): Additional context to guide the response.

        Returns:
            AIResponse: Structured response containing generated text,
                        provider name, model, and execution time.

        Raises:
            Exception: If Groq API errors occur (translated via _handle_exception).
        """
        start = time.perf_counter()
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": context},
                ],
                temperature=settings.temperature,
            )

            content = response.choices[0].message.content
            execution_time = int((time.perf_counter() - start) * 1000)

            return AIResponse(
                content=content,
                provider="groq",
                model=self.model,
                execution_time_ms=execution_time,
            )
        except Exception as ex:
            self._handle_exception(ex)

    def generate_json(self, prompt: str, context: str) -> AIResponse:
        """
        Generate a JSON response using Groq.

        Args:
            prompt (str): Input prompt for the AI provider.
            context (str): Additional context to guide the response.

        Returns:
            AIResponse: Structured response containing generated JSON.
        """
        return self.generate_text(prompt, context)

    def health_check(self) -> bool:
        """
        Verify provider availability.

        Returns:
            bool: True if Groq client responds successfully, False otherwise.
        """
        try:
            self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=1,
            )
            return True
        except Exception:
            return False

    def _handle_exception(self, ex: Exception) -> None:
        """
        Convert Groq exceptions into framework exceptions.

        Args:
            ex (Exception): Original Groq exception.

        Raises:
            Exception: Currently re-raises the original exception.
                       (Can be extended to map specific Groq errors
                       into framework-specific exceptions.)
        """
        raise ex
