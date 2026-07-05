"""
Utilities for parsing AI provider responses.

Provides helper methods to safely extract data from responses
returned by AI providers. Ensures consistent handling of empty
or malformed responses by raising framework-specific exceptions.
"""

from ai_resume_analyzer.ai.exceptions import InvalidResponseError


class ResponseParser:
    """
    Helper methods for extracting data from AI provider responses.

    Responsibilities:
        - Provide a unified way to extract text content.
        - Validate that responses contain usable data.
        - Raise framework exceptions when responses are invalid.
    """

    @staticmethod
    def extract_text(response: object) -> str:
        """
        Extract text from an AI provider response.

        Args:
            response (object): AI provider response object.

        Returns:
            str: Extracted text content.

        Raises:
            InvalidResponseError: If no text is found in the response.
        """
        text = getattr(response, "text", None)

        if not text:
            raise InvalidResponseError("AI provider returned an empty response.")

        return text
