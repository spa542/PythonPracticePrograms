from connections import get_connection
import psycopg2

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email TEXT, 
    subject TEXT, message TEXT);"""

INSERT_INFO = """INSERT INTO users (email, subject, message) VALUES (%s, %s, %s);"""

# Class to maintain and run queries of information sent

class Query:
    def __init__(self, email : str, subject : str, message : str):
        self.email = email
        self.subject = subject
        self.message = message

    def create_tables(self):
        with get_connection() as connection:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(CREATE_TABLE)

    def insert_contact_info(self):
        with get_connection() as connection:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(INSERT_INFO, (self.email, self.subject, self.message))
