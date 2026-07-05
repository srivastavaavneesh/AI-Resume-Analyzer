"""
Schema layer for AI Resume Analyzer.

Defines the request and response models used in the API.
These schemas act as data contracts between the API layer and
the service layer, ensuring validation, consistency, and
structured outputs across the application.

Responsibilities:
    - Input validation: Guarantee uploaded resumes and parsed data
      meet expected formats before processing.
    - Response shaping: Provide predictable, structured outputs
      for API endpoints (e.g., extracted text, parsed resume fields).
    - Data contracts: Serve as the single source of truth for how
      data flows between routes, services, and external clients.

Included Schemas:
    - ResumeExtractionResponse: Holds extracted text from uploaded resumes.
    - ResumeData: Parsed resume data with structured fields (name, email, skills, etc.).
    - ParsedResume: Rich structured representation of resume content
      for downstream analysis and ATS scoring.
"""
