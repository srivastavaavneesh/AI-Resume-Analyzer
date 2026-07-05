# -----------------------------------------------------------------------------
# File: Dockerfile
# Purpose: Builds the Docker image for the AI Resume Analyzer project.
#          Sets up Python environment, installs dependencies, configures user,
#          exposes service port, and defines healthcheck + startup command.
# -----------------------------------------------------------------------------

FROM python:3.13-slim

# Prevent Python from writing .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy all project files into container
COPY . .

# Install dependencies from setup.py / pyproject.toml
RUN pip install --no-cache-dir .

# Create non-root user for security
RUN useradd -m appuser
USER appuser

# Expose application port
EXPOSE 8000

# Healthcheck: verifies API is responding on /health endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Start FastAPI app with Uvicorn
CMD [ "uvicorn", "ai_resume_analyzer.main:app", "--host", "0.0.0.0", "--port", "8000" ]