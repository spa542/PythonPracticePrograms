import psycopg2

url = "postgres://nkauskyw:t3dy8ngEN6VuXyX-1G2-Okr4dXSYWKOv@ruby.db.elephantsql.com:5432/nkauskyw"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()
