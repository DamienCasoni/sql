# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sqlite3

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.executescript("""
        CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);
    """)
    
    population = (
        ('Jean-Baptiste Zorg', 'Human', 122),
        ('Korben Dallas', 'Meat Popsicle', 100),
        ("Ak'not", "Mangalore", -5)
    )

    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", population)
    
    c.execute("UPDATE Roster SET Species=? WHERE Name=?",('Human', 'Korben Dallas'))

    c.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
    
    for row in c.fetchall():
        print row