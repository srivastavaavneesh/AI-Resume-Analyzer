"""
Base exception for the AI Resume Analyzer.

Defines the root exception class for all custom application errors.
All other domain-specific exceptions inherit from this base class,
ensuring consistency and centralized error handling.
"""


class BaseApplicationException(Exception):
    """
    Base exception class for all custom application exceptions.

    Responsibilities:
        - Provide a common parent for all custom exceptions.
        - Store a human-readable error message.
        - Allow consistent handling of application-specific errors
          across API routes and services.

    Attributes:
        message (str): Human-readable error message describing the issue.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize the exception.

        Args:
            message (str): Human-readable error message.
        """
        super().__init__(message)
        self.message = message
