import pytest
from database.db_connection import get_connection\

@pytest.fixture
def db_connection():
    conn = get_connection()
    yield conn
    conn.close()