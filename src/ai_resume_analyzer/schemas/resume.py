"""
Resume schemas.
"""

from pydantic import BaseModel


class ResumeExtractionResponse(BaseModel):
    """
    Response model for resume extraction.
    """

    message: str
    extracted_text: str


class ResumeData(BaseModel):
    """
    Parsed resume data.
    """

    extracted_text: str

    name: str | None = None

    email: str | None = None

    phone: str | None = None

    linkedin: str | None = None

    github: str | None = None

    skills: list[str] = []

    experience: list[str] = []

    education: list[str] = []

    projects: list[str] = []

    certifications: list[str] = []
