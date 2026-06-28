"""
This module defines custom exceptions related to file handling in the AI Resume Analyzer application.
"""

from ai_resume_analyzer.exceptions.base import BaseApplicationException


class FileTooLargeException(BaseApplicationException):
    """Raised when the uploaded file exceeds the maximum allowed size."""

    def __init__(self, max_size_mb: int) -> None:
        """
        Initialize the exception.

        Args:
            message (str): Human-readable error message.
        """
        super().__init__(
            f"File size exceeds the maximum allowed size of {max_size_mb} MB."
        )


class EmptyFileException(BaseApplicationException):
    """Raised when the uploaded file is empty."""

    def __init__(self) -> None:
        """
        Initialize the exception.

        Args:
            message (str): Human-readable error message.
        """
        super().__init__("The uploaded file is empty.")


class InvalidFileExtensionException(BaseApplicationException):
    """
    Raised when the uploaded file extension is not supported.
    """

    def __init__(self, extension: str) -> None:
        super().__init__(
            f"Unsupported file extension '{extension}'. "
            "Supported extensions are: .pdf and .docx."
        )


class CorruptedFileException(BaseApplicationException):
    """
    Raised when the uploaded document is corrupted.
    """

    def __init__(self) -> None:
        super().__init__("The uploaded document appears to be corrupted.")


class InvalidFileSignatureException(BaseApplicationException):
    """
    Raised when the uploaded file signature is invalid.
    """

    def __init__(self) -> None:
        super().__init__(
            "The uploaded file content does not match its declared file type."
        )
