from flask import Flask, render_template, request, redirect, send_file
import os
import csv
#from dotenv import load_dotenv
#from psycopg2.pool import SimpleConnectionPool
#import Query
app = Flask(__name__)
#load_dotenv() # Load the .env file
#database_url = os.environ["DATABASE_URL"] # Set the environment variable

#pool = SimpleConnectionPool(minconn=1, maxconn=15, dsn=database_url) # Create the connection pool

# Basic website transition

@app.route('/')
def my_home():
    return render_template('index.html');

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# Saving information from contact me page

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

def write_to_online_database(data):
    query = Query.Query(data["email"], data["subject"], data["message"])
    query.create_tables()
    query.insert_contact_info()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            #write_to_online_database(data)
            return redirect('/thankyou.html')
        except Exception as e:
            print(e)
            return 'Did not save to database, something went wrong, try again'
    else:
        return 'something went wrong. Try again!'

# Sending Zip Files

# Leiontif's Econ I/O Model
@app.route('/zip-file')
def return_file():
    return send_file('./static/assets/DownloadFiles/Project1Rosiak.zip')

# Spell Checker
@app.route('/zip-file2')
def return_file2():
    return send_file('./static/assets/DownloadFiles/Project2Rosiak.zip')

# Poll App
@app.route('/zip-file3')
def return_file3():
    return send_file('./static/assets/DownloadFiles/PollApp.zip')

# Password Checker
@app.route('/zip-file4')
def return_file4():
    return send_file('./static/assets/DownloadFiles/PasswordChecker.zip')
