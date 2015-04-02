# -*- coding: utf-8 -*-

import sqlite3

# create a database, connecting to an existing one works the same
connection = sqlite3.connect("test_database.db")
"""
To create a one-time-use database while you’re testing code or playing around 
use the special name :memory: to create the database in temporary RAM like so: 
connection = sqlite3.connect(':memory:')
"""

# create a Cursor object to execute commands on the SQL db & return results
c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

# insert values into each field of table People
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
"""
Some versions of SQL (including SQLite) only allow strings to be enclosed 
in single quotation marks, so it’s important not to switch these around.
"""

# to commit is mandatory to save our changes in the db
connection.commit()

# delete table People only if it exists, which avoid errors
c.execute("DROP TABLE IF EXISTS People")

# we should close db connections as we close files opened
connection.close()

######################################################
#
# ATTENTION : voir sqlite-02.py 
# on peut utiliser with-as pour les db
# et c'est mieux ! :)
#
######################################################