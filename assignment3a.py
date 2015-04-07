"""
spend some time mapping (drawing) out the workflow as a
first step.
In this application we will be performing aggregations on 100 integers.

assignment3a.py : 
Add 100 random integers, ranging from 0 to 100, 
to a new database called newnum.db 

Begin by writing out exactly what the program should do in plain English. 
These sentences will become the comments for your program.
"""

# -*- coding: utf-8 -*-

import sqlite3
import random

# connect to newnum.db & create a cursor
with sqlite3.connect("newnum.db") as connection:
    cursor = connection.cursor()
    
    # create a table named random_int
    cursor.execute("CREATE TABLE IF NOT EXISTS randomint(int INTEGER)")
    
    # generate 100 integers from range 0 to 100
    random_integers = tuple((random.randint(0, 100) for x in range(0, 100)))
    
    print random_integers
    
    # insert into random_int the 100 random integers
    for i in random_integers:
        cursor.execute("INSERT INTO randomint VALUES(?)", i)
    
    # dedent so it close & commit the database


