# AI Resume Analyzer

An AI-powered Resume Analyzer built with FastAPI, Google Gemini, Groq, Docker, and Render.

## Live Demo

> Add your Render URL here after deployment

```
https://ai-resume-analyzer-3ynl.onrender.com/
```

---

## Features

- AI Resume Parsing
- ATS Score Calculation
- AI Resume Summary
- PDF Resume Support
- DOCX Resume Support
- Gemini AI Integration
- Groq AI Fallback
- Health Check API
- Docker Support
- Render Deployment
- Unit Tested

---

## Tech Stack

- Python 3.13
- FastAPI
- Google Gemini
- Groq
- Docker
- Render
- PyPDF
- python-docx
- Pytest

---

## Project Structure

```
src/
│
├── ai/
├── api/
├── core/
├── prompts/
├── schemas/
├── services/
└── ui/

tests/

Dockerfile
docker-compose.yml
pyproject.toml
```

---

## APIs

| Endpoint | Description |
|----------|-------------|
| `/` | Home |
| `/docs` | Swagger UI |
| `/health` | Health Check |
| `/resume/analyze` | Analyze Resume |

---

## Run Locally

```bash
git clone <repo>

cd AI-Resume-Analyzer

python -m venv .venv

pip install -e .

uvicorn ai_resume_analyzer.main:app --reload
```

---

## Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

## Testing

```bash
pytest

pytest --cov=src/ai_resume_analyzer
```

Current Coverage

```
72%
```

---

## Deployment

Hosted on Render using Docker.

---

## Roadmap

- AI Resume Analyzer ✅
- Multi Provider AI ✅
- ATS Scoring ✅
- Resume Summary ✅
- Docker ✅
- Render Deployment ✅

Future

- Resume Recommendation Engine
- Interview Question Generator
- Resume Improvement Suggestions

---

## Author

Avneesh Srivastava

AI Engineering Roadmap Project