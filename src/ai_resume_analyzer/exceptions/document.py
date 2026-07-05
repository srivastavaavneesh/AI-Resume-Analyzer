"""
Document-related exceptions.

Defines custom exceptions for handling document-specific errors
in the AI Resume Analyzer. These exceptions provide meaningful
feedback when uploaded documents cannot be processed correctly.
"""

from ai_resume_analyzer.exceptions.base import BaseApplicationException


class UnsupportedDocumentException(BaseApplicationException):
    """
    Raised when an unsupported document type is uploaded.

    Responsibilities:
        - Triggered when the uploaded file's MIME type is not supported.
        - Helps enforce allowed formats (PDF and DOCX).

    Attributes:
        content_type (str): The MIME type of the uploaded document.
    """

    def __init__(self, content_type: str) -> None:
        """
        Initialize the exception.

        Args:
            content_type (str): Uploaded document MIME type.
        """
        super().__init__(
            f"Unsupported document type: {content_type}. Supported types are: PDF and DOCX."
        )


class CorruptedDocumentException(BaseApplicationException):
    """
    Raised when the uploaded document is corrupted.

    Responsibilities:
        - Triggered when the document cannot be parsed or read.
        - Provides a clear error message for monitoring and debugging.
    """

    def __init__(self) -> None:
        super().__init__("The uploaded document is corrupted or unreadable.")


class PasswordProtectedDocumentException(BaseApplicationException):
    """
    Raised when the uploaded PDF is password protected.

    Responsibilities:
        - Triggered when a PDF cannot be opened due to encryption.
        - Ensures unsupported password-protected files are flagged early.
    """

    def __init__(self) -> None:
        super().__init__("Password-protected documents are not supported.")
