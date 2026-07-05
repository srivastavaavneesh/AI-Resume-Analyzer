"""
AI Response Schema.

Defines the standard response model returned by every AI provider.
Ensures consistency in how generated content, metadata, and execution
details are represented across the application.
"""

from pydantic import BaseModel


class AIResponse(BaseModel):
    """
    Standard response returned by every AI provider.

    Responsibilities:
        - Provide a unified schema for AI outputs.
        - Capture both content and metadata (tokens, execution time).
        - Ensure downstream services can rely on consistent fields.

    Attributes:
        content (str): The generated text or JSON content.
        provider (str): Name of the AI provider (e.g., "gemini", "groq").
        model (str): Model identifier used by the provider.
        input_tokens (int): Number of tokens consumed from the input prompt.
        output_tokens (int): Number of tokens generated in the response.
        execution_time_ms (int): Execution time in milliseconds.
        finish_reason (str): Reason why generation finished (e.g., "stop", "length").
    """

    content: str
    provider: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    execution_time_ms: int = 0
    finish_reason: str = ""
