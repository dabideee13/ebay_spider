import os
import psycopg2
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="module")
def db_connection():
    connection = psycopg2.connect(
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST")
    )
    yield connection

    connection.close()
