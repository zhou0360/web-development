# "Database code" for the DB Forum.

import psycopg2, bleach # Bleach is intended for sanitizing text from untrusted sources. I

def get_posts():
	# connect to the database 
	connection = psycopg2.connect(database="forum")

	# 1) Declare a cursor object that defines a result set 
	crsr = connection.cursor()

	# 2) Open the cursor to establish the result: return all the entries from the database
	crsr.execute("SELECT content, time FROM posts order by time desc")

	# 3) Fetch the data into local variables as needed from the cursor, one row at a time.
	posts = crsr.fetchall() 

	# 4) Close the cursor when done.
	"""db.close() is called before the get_posts function returns."""
	connection.close()

	return posts

def add_post(content):
	# connect to the database 
	connection = psycopg2.connect(database="forum")

	# declare a cursor object 
	crsr = connection.cursor()

	# Insert new POSTS to the database 
	crsr.execute("INSERT INTO posts VALUES (%s)", (content,) ) # tuple 

	# Save the changes to the database permanently 
	connection.commit()

	connection.close()
	



