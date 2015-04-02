# -*- coding: utf-8 -*-

# INSERT Command (it's about learning that...)

import sqlite3

with sqlite3.connect("new.db") as connection:
# better than: connection = sqlite3.connect("new.db")
# we still need to create a cursor:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 80000)")


# no need to commit the changes with the with-as above
# conn.commit()

# no need to close either! :D
# conn.close()       