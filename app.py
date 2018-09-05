# app.py - controller
from flask import Flask, render_template, request, sessions, flash, redirect, url_for, g

# imports
import sqlite3


# configuration
DATABASE = "blog.db"
SECRET_KEY = "hard_to_guess"
USERNAME = "admin"
PASSWORD = "admin"

app = Flask(__name__)

app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200

    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = "Invalid credentials. Please try again."
            status_code = 401
        else:
            sessions['logged_in'] = True
            return redirect(url_for('main'))

    return render_template("login.html", error=error)



@app.route('/main')
def main():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
