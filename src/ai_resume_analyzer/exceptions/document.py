"""
Document-related exceptions.
"""

from ai_resume_analyzer.exceptions.base import BaseApplicationException

class UnsupportedDocumentException(BaseApplicationException):
    """Raised when an unsupported document type is uploaded.
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
    """

    def __init__(self) -> None:
        super().__init__(
            "The uploaded document is corrupted or unreadable."
        )

class PasswordProtectedDocumentException(BaseApplicationException):
    """
    Raised when the uploaded PDF is password protected.
    """

    def __init__(self) -> None:
        super().__init__(
            "Password-protected documents are not supported."
        )