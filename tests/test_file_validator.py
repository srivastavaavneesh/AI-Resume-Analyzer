"""
Test for FileValidator
"""

from io import BytesIO

import pytest

from ai_resume_analyzer.core.constants import FileConstants
from ai_resume_analyzer.core.file_validator import FileValidator
from ai_resume_analyzer.exceptions import (
    EmptyFileException,
    InvalidFileExtensionException,
    UnsupportedDocumentException,
    FileTooLargeException
    )
from tests.conftest import create_upload_file

def test_validate_content_type_unsupported(create_upload_file):
    """
    Should raise exception for unsupported content type.
    """
    
    file = create_upload_file(
        filename="resume.txt",
        content=b"Hello",
        content_type="text/plain",
    )
    
    with pytest.raises(UnsupportedDocumentException):
        FileValidator.validate(file)
        
def test_validate_empty_file(create_upload_file):
    """
    Should raise exception for an empty file.
    """

    file = create_upload_file(
        filename="resume.pdf",
        content=b"",
        content_type="application/pdf",
    )

    with pytest.raises(EmptyFileException):
        FileValidator.validate(file)

def test_validate_invalid_extension(create_upload_file):
    """
    Should raise exception for an unsupported file extension.
    """
    file = create_upload_file(
        filename="resume.txt",
        content=b"%PDF-1.4",
        content_type= "application/pdf",
    )
    with pytest.raises(InvalidFileExtensionException):
        FileValidator.validate(file)

def test_validate_file_too_large(create_upload_file):
    """
    Should raise exception when the file exceeds the maximum size.
    """

    large_content = b"a" * ((FileConstants.MAX_FILE_SIZE_MB * 1024 * 1024) + 1)

    file = create_upload_file(
        filename="resume.pdf",
        content=large_content,
        content_type="application/pdf",
    )

    with pytest.raises(FileTooLargeException):
        FileValidator.validate(file)