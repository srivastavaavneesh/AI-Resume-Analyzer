"""
Service layer for AI Resume Analyzer.

This package contains the business logic that powers the application.
Responsibilities include:
    - Resume parsing: Extracting raw text from PDF/DOCX resumes.
    - Skill extraction: Identifying and structuring candidate skills.
    - ATS scoring: Evaluating resumes against job descriptions for ATS compatibility.
    - AI-based analysis: Leveraging AI models to generate summaries, recommendations,
      and interview insights.

The service layer acts as the bridge between API routes and core utilities,
ensuring separation of concerns and maintainable architecture.
"""
