# sql.py - Create a SQLite3 table and populate it with data

import sqlite3


# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:

    # get a cursor object used to execute SQL commands
    cursor = connection.cursor()

    # create the table
    cursor.execute("DROP TABLE IF EXISTS posts")
    cursor.execute("CREATE TABLE posts (title TEXT, post TEXT)")

    posts = [
        ("Good", "I'm good."),
        ("Well", "I'm well."),
        ("Excellent", "I'm excellent."),
    ]

    # insert dummy data into the table
    cursor.executemany("INSERT INTO posts VALUES(?, ?)", posts)
