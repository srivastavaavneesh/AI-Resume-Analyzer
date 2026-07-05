"""
Unit tests for the /health endpoint.
"""


def test_health_check(client):
    """
    Verify that the /health endpoint is reachable and returns
    the expected application metadata.
    """
    response = client.get("/health")

    # The endpoint should respond with HTTP 200
    assert response.status_code == 200

    body = response.json()

    # The response body should contain correct health details
    assert body["status"] == "healthy"
    assert body["app"] == "AI Resume Analyzer"
    assert body["version"] == "0.1.0"
