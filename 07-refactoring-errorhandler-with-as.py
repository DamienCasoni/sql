# -*- coding: utf-8 -*-

# INSERT command with Error Handler

# import the sqlite3 library
import sqlite3


with sqlite3.connect("07-refactor.db") as conn:

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE populations
    (city TEXT,
    state TEXT,
    population INT)   
    """)

    try:
        # insert data
        cursor.execute(
        "INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
        cursor.execute(
        "INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")
        print "Everything went fine!"
        
    except sqlite3.OperationalError:
        print "Oops! Something went wrong. Try again..."