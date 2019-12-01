import sqlite3

def show_all():
	conn= sqlite3.connect('customers.db')
	c=conn.cursor()
	c.execute("SELECT rowid,* FROM customers")
	items= c.fetchall()
	for item in items:
		print(item)
	conn.commit()
	conn.close()

def add_one(first,last,email):
	conn=sqlite3.connect('customers.db')
	c=conn.cursor()
	c.execute("""INSERT INTO customers VALUES 
		(?,?,?)
		""",(first, last, email))
	conn.commit()
	conn.close()

def delete_one(id):
	conn=sqlite3.connect('customers.db')
	c=conn.cursor()
	c.execute('DELETE FROM customers WHERE rowid=(?)',str(id))
	conn.commit()
	conn.close()

def add_many(many_records):
	conn=sqlite3.connect('customers.db')
	c=conn.cursor()
	c.executemany("""
		INSERT INTO customers VALUES (?,?,?)
		""",many_records)
	conn.commit()
	conn.close()

def email_lookup(mail):
	conn=sqlite3.connect('customers.db')
	c=conn.cursor()
	c.execute("SELECT * FROM customers WHERE email_address=(?)",
		(mail,))
	items = c.fetchall()
	for item in items:
		print(item)
	conn.commit()
	conn.close()