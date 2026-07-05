"""
API layer for AI Resume Analyzer.

Defines the REST API endpoints and request/response handling
for resume upload, parsing, ATS scoring, and text extraction.

Responsibilities:
    - Act as the interface between the frontend and the service layer.
    - Expose endpoints for uploading resumes (PDF/DOCX).
    - Handle parsing requests and return structured resume data.
    - Provide ATS scoring results and improvement suggestions.
    - Support text extraction for downstream AI analysis.
    - Ensure consistent request/response schemas across the application.

Endpoints (planned/implemented):
    - /resume/upload: Upload and validate resume files.
    - /resume/analyze: Parse and analyze resume content.
    - /resume/ats-score: Calculate ATS score and provide feedback.
    - /resume/extract: Extract raw text from resumes.
"""
