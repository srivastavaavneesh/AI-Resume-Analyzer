"""
Global exception handlers.

Defines centralized exception handling for the AI Resume Analyzer.
Ensures that custom application exceptions are caught and returned
as structured JSON responses with appropriate HTTP status codes.
"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from ai_resume_analyzer.exceptions.base import BaseApplicationException


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers with the FastAPI application.

    Responsibilities:
        - Attach handlers for custom application exceptions.
        - Ensure consistent error responses across all API routes.
        - Provide meaningful feedback to clients in JSON format.

    Args:
        app (FastAPI): The FastAPI application instance.
    """

    @app.exception_handler(BaseApplicationException)
    async def handle_application_exception(
        request: Request, exc: BaseApplicationException
    ) -> JSONResponse:
        """
        Handle custom application exceptions.

        Responsibilities:
            - Catch exceptions derived from BaseApplicationException.
            - Return a JSON response with HTTP 400 status code.
            - Include the error message in the response body.

        Args:
            request (Request): The incoming HTTP request.
            exc (BaseApplicationException): The raised custom exception.

        Returns:
            JSONResponse: A structured error response containing:
                - status_code: 400 (Bad Request)
                - content: {"message": <error message>}
        """
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": exc.message},
        )
