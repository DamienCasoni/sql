# -*- coding: utf-8 -*-

# results where given with a 'u' in front of each string
# outputted because we used to print the entire string 
# rather than just the values.
# now we're removing unicode characters

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    c.execute("SELECT firstname, lastname from employees")
    
    # fetchall() retrieves all records from the query
    # and store them as a list of tuples
    rows = c.fetchall()
    
    print "fetchall the selection: ", rows, "\n"
    
    #output the row to the screen, row by row
    for r in rows:
        print r[0], r[1]