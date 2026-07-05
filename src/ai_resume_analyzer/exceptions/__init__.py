"""
Custom exceptions for the AI Resume Analyzer.

Defines application-specific exception classes used across the project.
These exceptions provide meaningful error handling for file validation,
document extraction, and general application errors.

Responsibilities:
    - Centralize exception definitions for maintainability.
    - Provide descriptive error types for different failure scenarios.
    - Ensure consistent error handling across API routes and services.

Included Exceptions:
    - BaseApplicationException: Root exception class for all custom errors.
    - UnsupportedDocumentException: Raised when an unsupported document type is uploaded.
    - CorruptedDocumentException: Raised when a document is corrupted or unreadable.
    - PasswordProtectedDocumentException: Raised when a document is password-protected.
    - EmptyFileException: Raised when an uploaded file is empty.
    - FileTooLargeException: Raised when an uploaded file exceeds size limits.
    - InvalidFileExtensionException: Raised when a file has an invalid extension.
    - InvalidFileSignatureException: Raised when a file’s signature does not match its type.
"""

from ai_resume_analyzer.exceptions.base import BaseApplicationException
from ai_resume_analyzer.exceptions.document import (
    CorruptedDocumentException,
    PasswordProtectedDocumentException,
    UnsupportedDocumentException,
)
from ai_resume_analyzer.exceptions.file import (
    EmptyFileException,
    FileTooLargeException,
    InvalidFileExtensionException,
    InvalidFileSignatureException,
)

# __all__ defines the public API of this package.
# Only the listed exceptions will be exported when using:
#   from ai_resume_analyzer.exceptions import *
__all__ = [
    "BaseApplicationException",
    "UnsupportedDocumentException",
    "CorruptedDocumentException",
    "PasswordProtectedDocumentException",
    "EmptyFileException",
    "FileTooLargeException",
    "InvalidFileExtensionException",
    "InvalidFileSignatureException",
]
