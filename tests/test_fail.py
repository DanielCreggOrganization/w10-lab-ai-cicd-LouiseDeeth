import pytest
from hello_app.webapp import app

def test_fail():
    """This test now passes."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200  # Home route returns 200
