# -*- coding: utf-8 -*-

import sqlite3

connexion = sqlite3.connect("cars.db")

cursor = connexion.cursor()

cursor.execute("""CREATE TABLE inventory(
                Make TEXT,
                Model TEXT,
                Quantity INT)
                """)

connexion.close()