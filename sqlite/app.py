import database

#database.add_one('userx','lastx','last@lastx.com')
#database.delete_one(8)
many_records=[
	('seiya','pegaso','spegaso@gmail.com'),
	('shiryu','dragon','sdragon@gmail.com'),
	('ikki','fenix','ifenix@gmail.com')
]
#database.add_many(many_records)
database.email_lookup('ifenix@gmail.com')
#database.show_all()