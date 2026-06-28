"""
File validation utilities.
"""

from pathlib import Path

from fastapi import UploadFile

from ai_resume_analyzer.core.constants import FileConstants,ContentType
from ai_resume_analyzer.exceptions import (
    EmptyFileException,
    FileTooLargeException,
    InvalidFileExtensionException,
    UnsupportedDocumentException,
    InvalidFileSignatureException
)
class FileValidator:
    """
    Validates uploaded files.
    """
    
    @classmethod
    def validate(cls, file: UploadFile) -> None:   
        """
        Validate the uploaded file.

        Args:
            file: Uploaded file.

        Raises:
            BaseApplicationException:
            If any validation fails.
        """
        cls._validate_content_type(file)
        cls._validate_extension(file)
        cls._validate_file_size(file)
        cls._validate_empty_file(file)

    @classmethod
    def _validate_content_type(cls, file: UploadFile) -> None:
        """
        Validate the uploaded file content type.

        Args:
            file: Uploaded file.

        Raises:
            UnsupportedDocumentException: 
                If the file's content type is not supported.
        """
        if file.content_type not in FileConstants.SUPPORTED_CONTENT_TYPES:
            raise UnsupportedDocumentException(file.content_type)
        
    @classmethod
    def _validate_extension(cls, file: UploadFile) -> None:
        """
        Validate the uploaded file extension.

        Args:
            file: Uploaded file.

        Raises:
            InvalidFileExtensionException: 
                If the file's extension is not supported.
        """
        extension = Path(file.filename).suffix.lower()
        if extension not in FileConstants.SUPPORTED_EXTENSIONS:
            raise InvalidFileExtensionException(extension)
    
    @classmethod
    def _validate_file_size(cls, file: UploadFile) -> None:
        """
        Validate the uploaded file size.

        Args:
            file: Uploaded file.

        Raises:
            FileTooLargeException: If the file size exceeds the maximum allowed size.
        """
        
        file_size = cls._get_file_size(file)
        max_size = FileConstants.MAX_FILE_SIZE_MB * 1024 * 1024
        
        if file_size > max_size:
            raise FileTooLargeException(FileConstants.MAX_FILE_SIZE_MB)

    @classmethod
    def _validate_empty_file(cls, file: UploadFile) -> None:
        """
        Validate that the uploaded file is not empty.   
        """
        if cls._get_file_size(file) == 0:
            raise EmptyFileException()
    
    @staticmethod    
    def _get_file_size(file: UploadFile) -> int:
        """
        Get the size of the uploaded file in megabytes.

        Args:
            file: Uploaded file.
        Returns:
            int: File size in megabytes.
        """
        file.file.seek(0, 2)  # Move to the end of the file
        file_size = file.file.tell()  # Get the current position (file size)
        file.file.seek(0)  # Reset the file pointer to the beginning
        return file_size  # return bytes
    
    @classmethod
    def _validate_content_type_extension(cls, file: UploadFile) -> None:
        """
        Ensure the MIME type matches the file extension.

        Args:
            file: Uploaded file.

        Raises:
            InvalidFileExtensionException: 
                If the file's extension is not supported.
        """
        extension = Path(file.filename).suffix.lower()
        
        expected = FileConstants.CONTENT_TYPE_TO_EXTENSION.get(
        file.content_type
        )
        
        if expected != extension:
            raise InvalidFileExtensionException(extension)
        
    @classmethod
    def _validate_magic_bytes(cls, file: UploadFile) -> None:
        """
        Validate the uploaded file signature.

        Args:
            file: Uploaded file.

        Raises:
            InvalidFileSignatureException: 
                If the file's magic bytes do not match the expected magic bytes for its extension.
        """
        header = file.file.read(4)
        file.file.seek(0)
        
        if file.content_type == ContentType.PDF:
            if not header.startswith(FileConstants.PDF_MAGIC_BYTES):
                raise InvalidFileSignatureException()
            
        elif file.content_type == ContentType.DOCX:
            if not header.startswith(FileConstants.PDF_MAGIC_BYTES):
                raise InvalidFileSignatureException()
