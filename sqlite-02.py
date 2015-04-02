# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sqlite3

people_values = (
    ('Ron', 'Obvious', 42),
    ('Luigi', 'Vercotti', 43),
    ('Arthur', 'Belling', 28)
)

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    # .executescript() permet de lancer plus d'une ligne SQL à la fois
    # contrairement à .execute qui ne lance qu'une ligne
    c.executescript("""
        DROP TABLE IF EXISTS People;
        CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
    """)
    # Execute many SIMILAR statements with the executemany() method
    # and supplying a tuple of tuples
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)   
    """
    (?, ?, ?) act as place-holders for the tuples in people_values 
    this is called a **parameterized statement**
    For security reasons you should always use parameterized SQL statements. 
    This prevent “SQL injection” attack.
    """
    # select all first & last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    # fetchone() retrieve one result at a time of a SQL query (like read)
    # fetchall() retrieve all results of a SQL query (like readline)
    for row in c.fetchall():  
        print row  # (u'Ron', u'Obvious')
                   # (u'Luigi', u'Vercotti')
                   # on évite les 'u' avec l'import unicode_literals