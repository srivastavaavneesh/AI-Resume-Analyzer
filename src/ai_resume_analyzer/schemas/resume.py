
from pydantic import BaseModel


class ResumeExtractionResponse(BaseModel):
    """
    Response model for resume extraction.
    """
    message: str
    extracted_text: str