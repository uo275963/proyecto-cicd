import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """Test que verifica el endpoint de salud"""
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'


def test_data_endpoint(client):
    """Test que verifica el endpoint de datos"""
    response = client.get('/api/data')
    assert response.status_code == 200
    assert 'items' in response.json
    assert len(response.json['items']) == 3