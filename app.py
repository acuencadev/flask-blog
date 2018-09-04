# app.py - controller
from flask import Flask, render_template, request, sessions, flash, redirect, url_for, g

# imports
import sqlite3


# configuration
DATABASE = "blog.db"

app = Flask(__name__)

app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/main')
def login():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
