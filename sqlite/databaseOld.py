import sqlite3
#conn = sqlite3.connect(':memory:') in memory db
conn = sqlite3.connect('customers.db')
#create cursor to act on database
cursor = conn.cursor()
#create table
#use docstring 6 " to insert text in free format and multiple lines
cursor.execute("""CREATE TABLE customers (
	first_name text,
	last_name text,
	email_address text
)""")
# sqlite3 datatypes  null, integer,real, text, blob
#commit our command
conn.commit()

#close connection
conn.close()
