"""
Tests for Flask Application
"""
import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test home page returns 200."""
    response = client.get('/')
    assert response.status_code == 200


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'


def test_app_info(client):
    """Test app info endpoint."""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app'] == 'Flask CI/CD Demo'
    assert 'version' in data
