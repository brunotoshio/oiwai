""" Tests for endpoints
"""

from main import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as c:
        yield c


class TestHelloWorld:
    """ Test for GET /
    """
    def test_hello_world(self, client):
        response = client.get('/')

        assert 'Hello, World!' in str(response.data)


class TestPostParties:
    """ Tests for POST /parties
    """
    def test_post_parties(self, client):
        response = client.post('/parties', data={'name': 'test'})

        assert 'OK' in str(response.data)

    def test_missing_name(self, client):
        response = client.post('/parties', data={'name': ''})

        assert 'name is required' in str(response.data)
