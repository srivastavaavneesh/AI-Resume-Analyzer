"""Base exception for the AI Resume Analyzer."""

class BaseApplicationException(Exception):
    """Base exception class for all custom application exceptions.
    
    """
    def __init__(self, message: str)-> None:
        """
        Initialize the Exception.

        Args:
            message (str): Human-readable error message.
        """
        super().__init__(message)
        self.message = message