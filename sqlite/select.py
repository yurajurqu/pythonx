import sqlite3
#conn = sqlite3.connect(':memory:') in memory db
conn = sqlite3.connect('customers.db')
#create cursor to act on database
cursor = conn.cursor()

#create table
#use docstring 6 " to insert text in free format and multiple lines
cursor.execute("SELECT * FROM  customers")
#cursor.fetchone()
#cursor.fetchmany(3)
print(cursor.fetchall())
# sqlite3 datatypes  null, integer,real, text, blob
#commit our command
conn.commit()

#close connection
conn.close()
