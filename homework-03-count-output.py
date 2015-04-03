# -*- coding: utf-8 -*-

# INSTRUCTIONS
# Using the COUNT() function, calculate the total number of orders 
# for each make and model.
# Output the car’s make and model on one line, 
# the quantity on another line, 
# and the order count on the next line.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()
      
  # create a dictionary of sql queries
    sql = {'Focus count'    : "SELECT count(make) FROM orders WHERE model = 'Focus'",
            'Civic count'   : "SELECT count(make) FROM orders WHERE model = 'Civic'",
            'Ranger count'  : "SELECT count(make) FROM orders WHERE model = 'Ranger'",
            'Accord count'  : "SELECT count(make) FROM orders WHERE model = 'Accord'",
            'Avenger count' : "SELECT count(make) FROM orders WHERE model = 'Avenger'",}

    # run each sql query item in the dictionary
    for keys, values in sql.iteritems():

        # run sql
        cursor.execute(values)

        # fetchone() retrieves one record from the query
        result = cursor.fetchone()

        # output the result to screen
        print keys + ":", result[0]