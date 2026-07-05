"""
Resume Parser Service.

Extracts structured information from resume text such as name, email,
phone number, LinkedIn/GitHub profiles, skills, and major sections
(education, experience, projects, certifications).
"""

import re

from ai_resume_analyzer.schemas.parsed_resume import ParsedResume


class ParserService:
    """
    Service responsible for parsing resume text into structured fields.

    Uses regex patterns and keyword matching to identify common resume
    attributes. Provides helper methods for extracting specific fields
    and sections, then aggregates them into a ParsedResume schema.
    """

    # Predefined skill keywords to detect in resumes
    SKILL_KEYWORDS = [
        "Python",
        "C#",
        ".NET",
        "ASP.NET",
        "MVC",
        "SQL",
        "Azure",
        "Docker",
        "Kubernetes",
        "Git",
        "GitHub",
        "REST API",
        "FastAPI",
        "Java",
        "JavaScript",
        "TypeScript",
        "Angular",
        "React",
        "HTML",
        "CSS",
        "Machine Learning",
        "Artificial Intelligence",
        "OpenAI",
        "LangChain",
        "LangGraph",
    ]

    @staticmethod
    def extract_name(text: str) -> str | None:
        """
        Extract candidate name from resume text.

        Logic:
            - Scan first 10 lines
            - Skip empty lines, overly long lines, lines with digits or '@'
            - Accept lines with 2–3 words (likely a name)

        Args:
            text (str): Resume text

        Returns:
            str | None: Candidate name if found, else None
        """
        lines = text.splitlines()

        for line in lines[:10]:
            line = line.strip()
            if (
                not line
                or len(line) > 40
                or any(ch.isdigit() for ch in line)
                or "@" in line
            ):
                continue
            if len(line.split()) in (2, 3):
                return line
        return None

    @staticmethod
    def extract_email(text: str) -> str | None:
        """Extract email address using regex."""
        match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
        return match.group(0) if match else None

    @staticmethod
    def extract_phone(text: str) -> str | None:
        """Extract phone number (supports India +91, US +1, or plain 10-digit)."""
        patterns = [r"(\+91[\s-]?\d{10})", r"(\+1[\s-]?\d{10})", r"(\d{10})"]
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
        return None

    @staticmethod
    def extract_linkedin(text: str) -> str | None:
        """Extract LinkedIn profile URL."""
        match = re.search(
            r"(https?://)?(www\.)?linkedin\.com/[^\s]+", text, re.IGNORECASE
        )
        return match.group(0) if match else None

    @staticmethod
    def extract_github(text: str) -> str | None:
        """Extract GitHub profile URL."""
        match = re.search(
            r"(https?://)?(www\.)?github\.com/[^\s]+", text, re.IGNORECASE
        )
        return match.group(0) if match else None

    def extract_skills(self, text: str) -> list[str]:
        """
        Extract skills by keyword matching.

        Args:
            text (str): Resume text

        Returns:
            list[str]: Unique sorted list of detected skills
        """
        found = []
        lower = text.lower()
        for skill in self.SKILL_KEYWORDS:
            if skill.lower() in lower:
                found.append(skill)
        return sorted(set(found))

    @staticmethod
    def extract_section(text: str, heading: str) -> list[str]:
        """
        Extract section content based on heading.

        Logic:
            - Start capturing lines after heading match
            - Stop when encountering another uppercase heading

        Args:
            text (str): Resume text
            heading (str): Section heading (e.g., "education")

        Returns:
            list[str]: Lines belonging to the section
        """
        lines = text.splitlines()
        capture = False
        result = []

        for line in lines:
            current = line.strip()
            if not current:
                continue
            if capture:
                if current.isupper():
                    break
                result.append(current)
            if heading.lower() in current.lower():
                capture = True

        return result

    def parse(self, text: str) -> ParsedResume:
        """
        Parse resume text into structured ParsedResume schema.

        Args:
            text (str): Raw resume text

        Returns:
            ParsedResume: Structured resume data
        """
        return ParsedResume(
            name=self.extract_name(text),
            email=self.extract_email(text),
            phone=self.extract_phone(text),
            linkedin=self.extract_linkedin(text),
            github=self.extract_github(text),
            skills=self.extract_skills(text),
            education=self.extract_section(text, "education"),
            experience=self.extract_section(text, "experience"),
            projects=self.extract_section(text, "project"),
            certifications=self.extract_section(text, "certification"),
            extracted_text=text,
        )


# Singleton instance for reuse
parser_service = ParserService()
