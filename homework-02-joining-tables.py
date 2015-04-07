# -*- coding: utf-8 -*-

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders
                    (make TEXT,
                    model TEXT,
                    order_date DATE)
                    """)
        
    orders = [
            ('Ford', 'Focus', '2014-01-22'),
            ('Ford', 'Focus', '2014-01-23'),
            ('Ford', 'Focus', '2014-01-24'),
            ('Honda', 'Civic', '2014-01-25'),
            ('Honda', 'Civic', '2014-01-26'),
            ('Honda', 'Civic', '2014-01-27'),
            ('Ford', 'Ranger', '2014-01-28'),
            ('Ford', 'Ranger', '2014-01-22'),
            ('Ford', 'Ranger', '2014-01-23'),
            ('Honda', 'Accord', '2014-01-24'),
            ('Honda', 'Accord', '2014-01-25'),
            ('Honda', 'Accord', '2014-01-26'),
            ('Ford', 'Avenger', '2014-01-27'),
            ('Ford', 'Avenger', '2014-01-28'),
            ('Ford', 'Avenger', '2014-01-22'),
        ]
            
    cursor.executemany("""INSERT INTO orders VALUES(?, ?, ?)""", orders)
    
    # output the car’s make and model on one line, the quantity on another line
    # and then the order_dates on subsequent lines below that
    cursor.execute("""SELECT inventory.make, inventory.model, 
                    inventory.quantity, 
                    orders.order_date
                    FROM inventory
                    INNER JOIN orders ON inventory.model = orders.model
                    """)

    rows = cursor.fetchall()

    for r in rows:
        print r[0], r[1]  # inventory.make, inventory.model
        print r[2]  # inventory.quantity, 
        print r[3]  # orders.order_date
        print