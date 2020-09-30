import pytest
from fastapi.testclient import TestClient

from explorer_api.main import app


@pytest.fixture
def test_client():
    return TestClient(app)
