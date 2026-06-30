"""
Resume Parser Service.

Extracts structured information from resume text.
"""

import re

from ai_resume_analyzer.schemas.parsed_resume import ParsedResume


class ParserService:
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
        lines = text.splitlines()

        for line in lines[:10]:
            line = line.strip()

            if not line:
                continue

            if len(line) > 40:
                continue

            if any(ch.isdigit() for ch in line):
                continue

            if "@" in line:
                continue

            if len(line.split()) in (2, 3):
                return line

        return None

    @staticmethod
    def extract_email(text: str) -> str | None:
        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        return match.group(0) if match else None

    @staticmethod
    def extract_phone(text: str) -> str | None:
        patterns = [
            r"(\+91[\s-]?\d{10})",
            r"(\+1[\s-]?\d{10})",
            r"(\d{10})",
        ]

        for pattern in patterns:
            match = re.search(pattern, text)

            if match:
                return match.group(0)

        return None

    @staticmethod
    def extract_linkedin(text: str) -> str | None:
        match = re.search(
            r"(https?://)?(www\.)?linkedin\.com/[^\s]+",
            text,
            re.IGNORECASE,
        )

        return match.group(0) if match else None

    @staticmethod
    def extract_github(text: str) -> str | None:
        match = re.search(
            r"(https?://)?(www\.)?github\.com/[^\s]+",
            text,
            re.IGNORECASE,
        )

        return match.group(0) if match else None

    def extract_skills(self, text: str) -> list[str]:
        found = []

        lower = text.lower()

        for skill in self.SKILL_KEYWORDS:
            if skill.lower() in lower:
                found.append(skill)

        return sorted(set(found))

    @staticmethod
    def extract_section(text: str, heading: str) -> list[str]:
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


parser_service = ParserService()
