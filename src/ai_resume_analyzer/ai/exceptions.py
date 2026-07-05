"""
Custom exceptions for AI providers.

Defines application-specific exceptions for handling errors
that occur when interacting with external AI providers.
These exceptions provide meaningful error messages and
allow consistent error handling across the application.
"""


class AIProviderError(Exception):
    """
    Base exception for all AI provider errors.

    Responsibilities:
        - Serve as the root exception for provider-related errors.
        - Allow consistent handling of AI provider failures.
    """


class AuthenticationError(AIProviderError):
    """
    Raised when authentication with the AI provider fails.

    Typical causes:
        - Invalid API key.
        - Expired or missing credentials.
    """


class ProviderUnavailableError(AIProviderError):
    """
    Raised when the AI provider is unavailable.

    Typical causes:
        - Service downtime.
        - Network connectivity issues.
        - Provider maintenance.
    """


class RateLimitError(AIProviderError):
    """
    Raised when the AI provider rate limit is exceeded.

    Typical causes:
        - Too many requests in a short time.
        - Exceeding quota or usage limits.
    """


class InvalidResponseError(AIProviderError):
    """
    Raised when the AI provider returns an invalid response.

    Typical causes:
        - Malformed or incomplete response payload.
        - Unexpected data format.
        - Parsing errors in provider output.
    """
