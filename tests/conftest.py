import pymongo
import pytest


@pytest.fixture
def mongo():
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.test_db
    yield db
    client.drop_database('test_db')
