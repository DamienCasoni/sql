# -*- coding: utf-8 -*-

# SQL JOIN

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    # retrieve data
    # même si on détaille bien dans SELECT table.colonne
    # il faut quand même préciser FROM tables juste après
    # WHERE clause pour éliminer les duplicatas
    c.execute("""SELECT DISTINCT population.city, 
                population.population, regions.region 
            FROM population, regions
            WHERE population.city = regions.city 
            ORDER by population.city ASC
            """)
    
    rows = c.fetchall()
    
    print rows

    for r in rows:
        print "City: " + r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print "\n"
        