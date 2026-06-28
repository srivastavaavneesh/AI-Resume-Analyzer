"""
Shared pytest fixtures.
"""

from io import BytesIO

import pytest
from fastapi import UploadFile
from fastapi.testclient import TestClient

from ai_resume_analyzer.main import app


@pytest.fixture
def client() -> TestClient:
    """
    Create a reusable Fast API test client
    """
    return TestClient(app)


@pytest.fixture
def create_upload_file():
    """
    Factory fixture to create UploadFile instances for testing.
    """

    def _create(
        filename: str,
        content: bytes,
        content_type: str,
    ) -> UploadFile:
        return UploadFile(
            filename=filename,
            file=BytesIO(content),
            headers={"content-type": content_type},
        )

    return _create
