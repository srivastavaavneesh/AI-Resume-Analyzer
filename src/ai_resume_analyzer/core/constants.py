"""
Application constants.

Defines reusable constants for file handling and content type validation
in the AI Resume Analyzer. These constants ensure consistency across
services such as file validation, document extraction, and parsing.
"""


class ContentType:
    """
    Supported document MIME types.

    Responsibilities:
        - Provide canonical MIME type strings for supported formats.
        - Ensure consistent usage across validation and extraction services.

    Attributes:
        PDF (str): MIME type for PDF documents.
        DOCX (str): MIME type for DOCX (Word) documents.
    """

    PDF = "application/pdf"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


class FileConstants:
    """
    File upload related constants.

    Responsibilities:
        - Define maximum file size limits.
        - Specify supported content types and extensions.
        - Provide magic byte signatures for file type validation.

    Attributes:
        MAX_FILE_SIZE_MB (int): Maximum allowed file size in MB.
        SUPPORTED_CONTENT_TYPES (set[str]): Allowed MIME types (PDF, DOCX).
        SUPPORTED_EXTENSIONS (set[str]): Allowed file extensions (.pdf, .docx).
        PDF_MAGIC_BYTES (bytes): Magic bytes signature for PDF files.
        DOCX_MAGIC_BYTES (bytes): Magic bytes signature for DOCX files.
    """

    MAX_FILE_SIZE_MB = 10  # Maximum file size in megabytes

    SUPPORTED_CONTENT_TYPES = {
        ContentType.PDF,
        ContentType.DOCX,
    }

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".docx",
    }

    PDF_MAGIC_BYTES = b"%PDF"
    DOCX_MAGIC_BYTES = b"PK"
