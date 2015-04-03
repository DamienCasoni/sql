# -*- coding: utf-8 -*-

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

# Using the COUNT() function, calculate the total number of orders 
# for each make and model.
    
    cursor.execute("""
                        SELECT count(make) FROM orders;
                    """)
    cursor.execute("""                    
          SELECT count(model) FROM orders;
    """)
    
    result = cursor.fetchall()
    
    print result




# Output the car’s make and model on one line, 
# the quantity on another line, 
# and the order count on the next line.