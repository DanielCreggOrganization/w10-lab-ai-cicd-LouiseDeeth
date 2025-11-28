import pytest
from hello_app.webapp import app

def test_fail():
    """This test is designed to fail."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 404  # Should fail, home route returns 200
