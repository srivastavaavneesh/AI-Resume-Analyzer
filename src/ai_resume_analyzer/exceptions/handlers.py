"""
Global exception handlers.
"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from ai_resume_analyzer.exceptions.base import BaseApplicationException


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers.

    Args:
        app: The FastAPI application instance.
    """

    @app.exception_handler(BaseApplicationException)
    async def handle_application_exception(
        request: Request, exc: BaseApplicationException
    ) -> JSONResponse:
        """
        Handle custom application exceptions.
        """
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": exc.message},
        )
