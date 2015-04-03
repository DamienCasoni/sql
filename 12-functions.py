# -*- coding: utf-8 -*-

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    # a dictionary of SQL queries
    sql = {'average': "SELECT avg(population) FROM population",
            'maximum': "SELECT max(population) FROM population",
            'minimum': "SELECT min(population) FROM population",
            'sum': "SELECT sum(population) FROM population",
            'count': "SELECT count(city) FROM population"
            }
            
    # run each SQL query item in the dictionary
    for keys, values in sql.iteritems():
    
        c.execute(values)
        result = c.fetchone()
        # print result  # retourne un tuple (INT, vide)
        print keys + ":", result[0]
        