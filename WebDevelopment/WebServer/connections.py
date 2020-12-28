import server
from contextlib import contextmanager
import psycopg2

# Context manager for giving connections out from the connection pool

@contextmanager
def get_connection():
    connection = server.pool.getconn()

    try:
        yield connection
    finally:
        server.pool.putconn(connection)
