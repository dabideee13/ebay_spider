import pytest


def test_database_connection(db_connection):
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT 1")
        assert cursor.fetchone()[0] == 1
    except Exception as err:
        pytest.fail(f"Database connection failed: {err}")
