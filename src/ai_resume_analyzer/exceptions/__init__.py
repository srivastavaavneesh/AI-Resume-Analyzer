"""
Custom exceptions for the AI Resume Analyzer.
"""

from ai_resume_analyzer.exceptions.base import BaseApplicationException

from ai_resume_analyzer.exceptions.document import (
    UnsupportedDocumentException,
    CorruptedDocumentException,
    PasswordProtectedDocumentException,
)
from ai_resume_analyzer.exceptions.file import(
    EmptyFileException,
    FileTooLargeException,
    InvalidFileExtensionException,
    InvalidFileSignatureException,
)

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