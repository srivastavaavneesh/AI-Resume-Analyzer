"""
Unit tests for ATSService scoring functionality.
"""

from ai_resume_analyzer.schemas.resume import ResumeData
from ai_resume_analyzer.services.ats_service import ats_service


def test_ats_score_complete_resume():
    """
    Verify that calculate_score returns a high score and grade 'A+'
    when the resume contains all major sections with sufficient detail.
    """
    resume = ResumeData(
        extracted_text="Sample",
        name="John Doe",
        email="john@test.com",
        phone="9999999999",
        linkedin="linkedin.com/in/john",
        github="github.com/john",
        skills=[
            "Python",
            "FastAPI",
            "Docker",
            "Azure",
            "Git",
            "SQL",
            "C#",
            ".NET",
            "REST API",
            "LangChain",
        ],
        experience=["Software Engineer"],
        education=["B.Tech"],
        projects=["Resume Analyzer"],
        certifications=["AZ-204"],
    )

    result = ats_service.calculate_score(resume)

    # A complete resume should achieve a score of 90 or higher
    # and be graded as "A+".
    assert result["score"] >= 90
    assert result["grade"] == "A+"
