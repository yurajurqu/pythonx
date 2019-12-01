import sqlite3
#conn = sqlite3.connect(':memory:') in memory db
conn = sqlite3.connect('customers.db')
#create cursor to act on database
cursor = conn.cursor()
#create table
#use docstring 6 " to insert text in free format and multiple lines
cursor.execute("DELETE FROM customers WHERE rowid = 4")
conn.commit()

cursor.execute("SELECT rowid,* FROM  customers")
items=cursor.fetchall()
for item in items:
	print(item)
# sqlite3 datatypes  null, integer,real, text, blob
#commit our command
conn.commit()
#close connection
conn.close()
