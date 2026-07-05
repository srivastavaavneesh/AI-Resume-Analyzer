"""
File-related exceptions.

Defines custom exceptions for handling file validation errors
in the AI Resume Analyzer. These exceptions provide meaningful
feedback when uploaded files fail validation checks.
"""

from ai_resume_analyzer.exceptions.base import BaseApplicationException


class FileTooLargeException(BaseApplicationException):
    """
    Raised when the uploaded file exceeds the maximum allowed size.

    Responsibilities:
        - Triggered when file size is greater than the configured limit.
        - Provides a clear error message with the maximum size allowed.

    Attributes:
        max_size_mb (int): Maximum allowed file size in MB.
    """

    def __init__(self, max_size_mb: int) -> None:
        super().__init__(
            f"File size exceeds the maximum allowed size of {max_size_mb} MB."
        )


class EmptyFileException(BaseApplicationException):
    """
    Raised when the uploaded file is empty.

    Responsibilities:
        - Triggered when the file has zero bytes.
        - Ensures empty uploads are flagged early.
    """

    def __init__(self) -> None:
        super().__init__("The uploaded file is empty.")


class InvalidFileExtensionException(BaseApplicationException):
    """
    Raised when the uploaded file extension is not supported.

    Responsibilities:
        - Triggered when the file extension does not match supported types.
        - Helps enforce allowed formats (.pdf and .docx).

    Attributes:
        extension (str): The unsupported file extension.
    """

    def __init__(self, extension: str) -> None:
        super().__init__(
            f"Unsupported file extension '{extension}'. "
            "Supported extensions are: .pdf and .docx."
        )


class CorruptedFileException(BaseApplicationException):
    """
    Raised when the uploaded document is corrupted.

    Responsibilities:
        - Triggered when the file cannot be parsed or read.
        - Provides a clear error message for monitoring and debugging.
    """

    def __init__(self) -> None:
        super().__init__("The uploaded document appears to be corrupted.")


class InvalidFileSignatureException(BaseApplicationException):
    """
    Raised when the uploaded file signature is invalid.

    Responsibilities:
        - Triggered when the file content does not match its declared type.
        - Ensures files with mismatched headers are rejected.
    """

    def __init__(self) -> None:
        super().__init__(
            "The uploaded file content does not match its declared file type."
        )
