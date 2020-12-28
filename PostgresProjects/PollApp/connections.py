import os
from contextlib import contextmanager
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

DATABASE_PROMPT = "Enter the DATABASE_URL value or leave empty to load from .env file: "

database_url = input(DATABASE_PROMPT)
if not database_url:
    load_dotenv()
    database_url = os.environ["DATABASE_URL"]

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=database_url)

@contextmanager
def get_connection():
    connection = pool.getconn()

    try:
        yield connection
    finally:
        pool.putconn(connection)
