"""
Test for the health endpoint
"""


def test_health_check(client):
    """
    Verify that the health endpoint is reachable.
    """
    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["app"] == "AI Resume Analyzer"
    assert body["version"] == "0.1.0"
