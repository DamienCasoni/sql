# -*- coding: utf-8 -*-

# INSERT command with Error Handler

# import the sqlite3 library
import sqlite3

# create a new databae if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    # try with populationS instead of population
    cursor.executescript("""
        INSERT INTO populationS VALUES('New York City', 'NY', 8200000);
        INSERT INTO population VALUES('San Francisco', 'CA', 800000)
        """)
    
    # commit the changes
    conn.commit()
    
except sqlite3.OperationalError:
    print "Oops! Something went wrong. Try again..."


# close the database connection
conn.close()