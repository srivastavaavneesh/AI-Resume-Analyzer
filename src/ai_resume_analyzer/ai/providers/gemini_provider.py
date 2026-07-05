"""
Gemini AI Provider.

Implements the AIProvider interface using Google Gemini.
Handles text and JSON generation requests, provider health checks,
and exception translation into framework-specific errors.
"""

import time

from google import genai
from google.genai import types
from google.genai.errors import (
    APIError,
    ClientError,
    ServerError,
)

from ai_resume_analyzer.ai.exceptions import (
    AuthenticationError,
    InvalidResponseError,
    ProviderUnavailableError,
    RateLimitError,
)
from ai_resume_analyzer.ai.providers.base import AIProvider
from ai_resume_analyzer.ai.response_parser import ResponseParser
from ai_resume_analyzer.core.config import settings
from ai_resume_analyzer.core.logging.logger import get_logger
from ai_resume_analyzer.schemas.ai import AIResponse

logger = get_logger(__name__)


class GeminiProvider(AIProvider):
    """
    Google Gemini implementation of AIProvider.

    Responsibilities:
        - Initialize Gemini client with API key and model settings.
        - Generate text and JSON responses from prompts and context.
        - Perform health checks to verify provider availability.
        - Translate Gemini-specific exceptions into framework exceptions.

    Attributes:
        model (str): Gemini model name configured in settings.
        client (genai.Client): Gemini client instance.
    """

    def __init__(self):
        self.model = settings.gemini_model
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = genai.Client(api_key=settings.gemini_api_key)
            logger.info(f"Gemini Provider initialized ({self.model})")
        return self._client

    def generate_text(self, prompt: str, context: str) -> AIResponse:
        """
        Generate a text response using Gemini.

        Args:
            prompt (str): Input prompt for the AI provider.
            context (str): Additional context to guide the response.

        Returns:
            AIResponse: Structured response containing generated text,
                        provider name, model, and execution time.

        Raises:
            AuthenticationError, RateLimitError, ProviderUnavailableError,
            InvalidResponseError: If Gemini API errors occur.
        """
        start = time.perf_counter()
        try:
            logger.info("Calling Gemini model: %s", self.model)

            response = self.client.models.generate_content(
                model=self.model,
                contents=f"{prompt}\n\n{context}",
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=settings.temperature,
                    max_output_tokens=settings.max_tokens,
                ),
            )

            content = ResponseParser.extract_text(response)

            execution_time = int((time.perf_counter() - start) * 1000)
            logger.info("Gemini completed in %d ms", execution_time)

            return AIResponse(
                content=content,
                provider="gemini",
                model=self.model,
                execution_time_ms=execution_time,
            )
        except (ClientError, ServerError, APIError, Exception) as ex:
            self._handle_exception(ex)

    def generate_json(self, prompt: str, context: str) -> AIResponse:
        """
        Generate a JSON response using Gemini.

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
            bool: True if Gemini client responds successfully, False otherwise.
        """
        try:
            self.client.models.list()
            return True
        except Exception:
            return False

    def _handle_exception(self, ex: Exception) -> None:
        """
        Convert Gemini exceptions into framework exceptions.

        Args:
            ex (Exception): Original Gemini exception.

        Raises:
            AuthenticationError: If API key is invalid.
            RateLimitError: If quota or rate limits are exceeded.
            ProviderUnavailableError: If provider is unavailable.
            InvalidResponseError: If response is invalid.
        """
        logger.error("Gemini provider error: %s", ex)
        message = str(ex).lower()

        if "api key" in message:
            raise AuthenticationError(str(ex))
        if "quota" in message or "429" in message:
            raise RateLimitError(str(ex))
        if "503" in message:
            raise ProviderUnavailableError(str(ex))
        if "invalid" in message:
            raise InvalidResponseError(str(ex))

        raise ProviderUnavailableError(str(ex))
