"""
Parsed Resume Schema.

Defines the structured representation of a parsed resume.
This schema is used by the ParserService and ATSService to store
and analyze extracted resume information in a consistent format.
"""

from pydantic import BaseModel, Field


class ParsedResume(BaseModel):
    """
    Parsed resume data model.

    Represents structured information extracted from a resume.
    Provides a normalized schema for downstream services such as
    ATS scoring, skill extraction, and AI-based analysis.

    Attributes:
        name (str | None): Candidate's full name.
        email (str | None): Candidate's email address.
        phone (str | None): Candidate's phone number.
        linkedin (str | None): LinkedIn profile URL.
        github (str | None): GitHub profile URL.
        summary (str | None): Candidate's professional summary or objective.
        skills (list[str]): List of detected technical skills.
        education (list[str]): Lines of educational background.
        experience (list[str]): Lines of professional experience.
        projects (list[str]): Lines describing project work.
        certifications (list[str]): Lines describing certifications.
        extracted_text (str): Raw resume text.
    """

    name: str | None = None
    email: str | None = None
    phone: str | None = None
    linkedin: str | None = None
    github: str | None = None
    summary: str | None = None

    # Use Field with default_factory to avoid mutable default pitfalls
    skills: list[str] = Field(default_factory=list)
    education: list[str] = Field(default_factory=list)
    experience: list[str] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)

    extracted_text: str
