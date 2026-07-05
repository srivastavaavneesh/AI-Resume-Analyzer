"""
Application logger configuration.

Provides a centralized logger setup for the AI Resume Analyzer.
Ensures consistent logging format and log levels across modules.
"""

import logging


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger instance.

    Responsibilities:
        - Configure logging with a standard format and INFO level.
        - Provide module-specific loggers using the given name.
        - Ensure consistent logging output across the application.

    Args:
        name (str): Name of the logger, typically __name__ of the module.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    return logging.getLogger(name)
