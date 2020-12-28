import sqlite3

connection = sqlite3.connect("./data.db")

def create_table():
    with connection: # This is is a context manager, commits changes after block is done executing
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(f"INSERT INTO entries (content, date) VALUES (?, ?);", (entry_content, entry_date))

def get_entries():
    cursor = connection.execute("SELECT * FROM ENTRIES;")
    return cursor
