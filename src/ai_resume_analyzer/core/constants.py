"""
This module defines constants used throughout the application."""


class ContentType:
    """Supported document MIME types."""

    PDF = "application/pdf"

    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


class FileConstants:
    """File upload related constants."""

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
