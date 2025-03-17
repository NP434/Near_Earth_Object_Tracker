
import pytest
from app.data import get_data

@pytest.fixture
def data():
    returned_data = get_data()
    return returned_data

def test_get_data(data):
    assert data != None
