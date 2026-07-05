"""
Resume schemas.

Defines request and response models for resume-related API endpoints.
These schemas ensure consistent data contracts between the API layer
and the service layer, providing validation and structured outputs.
"""

from pydantic import BaseModel


class ResumeExtractionResponse(BaseModel):
    """
    Response model for resume extraction.

    Returned by the `/resume/upload` endpoint after processing
    an uploaded resume file.

    Attributes:
        message (str): Confirmation message about the extraction process.
        extracted_text (str): Raw text extracted from the uploaded resume.
    """

    message: str
    extracted_text: str


class ResumeData(BaseModel):
    """
    Parsed resume data.

    Represents structured information extracted from a resume.
    Used by services such as ATS scoring, parsing, and analysis.

    Attributes:
        extracted_text (str): Raw resume text.
        name (str | None): Candidate's full name.
        email (str | None): Candidate's email address.
        phone (str | None): Candidate's phone number.
        linkedin (str | None): LinkedIn profile URL.
        github (str | None): GitHub profile URL.
        skills (list[str]): List of detected technical skills.
        experience (list[str]): Lines of professional experience.
        education (list[str]): Lines of educational background.
        projects (list[str]): Lines describing project work.
        certifications (list[str]): Lines describing certifications.
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
