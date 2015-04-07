# -*- coding: utf-8 -*-

import sqlite3

def printing(rows):
    for r in rows:
        print r[0], r[1], r[2] 
    print "\n"

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()
    
    # homework 0: create a table
    cursor.execute("""DROP TABLE IF EXISTS inventory""")
    cursor.execute("""CREATE TABLE inventory (
                    Make TEXT, Model TEXT, Quantity INTEGER)
                    """)
        
    # homework 1: insert values in it
    data = [
    ('Ford', 'Focus', 1),
    ('Ford', 'Ranger', 3),
    ('Ford', 'Avenger', 4),
    ('Honda', 'Civic', 2),
    ('Honda', 'Accord', 4)    
    ]
    
    cursor.executemany("INSERT INTO inventory VALUES(?, ?, ?)", data)
    
    # homework 2: update the quantity on 2 of the records                   
    cursor.executescript("""
    UPDATE inventory SET Quantity=8 WHERE Make='Ford' AND Model='Ranger';
    UPDATE inventory SET Quantity=0 WHERE Make='Honda' AND Model='Civic';
    """)
    
    print "NEW DATA:"
    
    # output all the records from the table
    # NE PAS OUBLIER DE SELECT AVANT DE FETCHALL() !
    cursor.execute("SELECT * FROM inventory")
    printing(cursor)
    
    # homework 3: output only records that are Ford vehicules
    print 'Make Model Qty'
    print '--------------'
    cursor.execute("SELECT * FROM inventory WHERE Make='Ford'")
    printing(cursor)