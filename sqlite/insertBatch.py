import sqlite3
#conn = sqlite3.connect(':memory:') in memory db
conn = sqlite3.connect('customers.db')
#create cursor to act on database
cursor = conn.cursor()

many_customers=[
	('Wes','Brown','wbrown@brown.com'),
	('Steph','Kuewa','steph@kuewa.com'),
	('Dan','Pas','dan@pas.com')
]
#create table
#use docstring 6 " to insert text in free format and multiple lines
cursor.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

# sqlite3 datatypes  null, integer,real, text, blob
#commit our command
conn.commit()

#close connection
conn.close()
