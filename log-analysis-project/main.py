#Your task is to create a reporting tool that prints out reports (in plain text) 
#based on the data in the database. This reporting tool is a Python program 
#using the psycopg2 module to connect to the database.

import psycopg2

Q1 = 'Q1. What are the most popular three articles of all time?'

query1 = """select articles.title, count(log.id) as views
			from articles join log on log.path = concat('/article/', articles.slug)
			group by articles.title
			order by views desc
			limit 3"""

Q2 = 'Q2. Who are the most popular article authors of all time?'

query2 = """select authors.name, count(log.id) as views
			from log 
			join articles on log.path = concat('/article/', articles.slug)
			join authors on articles.author = authors.id 
			group by authors.id
			order by views desc 
			limit 3"""

Q3 = 'Q3. On which days did more than 1% of requests lead to errors?'

query3 = """select 
			to_char(log_date::date, 'Mon dd, yyyy') as log_date
			, to_char(100.0*error_rate, '999D99%') as error_rate

			from 
			(
				select 

				date_trunc('day', time) as log_date
				, sum(case when log.status like '%404%' then 1 else 0 end)::decimal/count(*) as error_rate
				--, to_char(100.0*(sum(case when log.status like '%404%' then 1 else 0 end))/count(*), '999D99%') as error_rate

				, sum(case when log.status like '%404%' then 1 else 0 end) as errors
				, count(*) as total_requests

				from log  

				group by date_trunc('day', time) 

			) t 

			where t.error_rate > 0.01"""

def get_ans(Q, query):
	# connect to the database 
	connection = psycopg2.connect(database="news")

	# 1) Declare a cursor object that defines a result set 
	crsr = connection.cursor()

	# 2) Open the cursor to establish the result: return all the entries from the database
	crsr.execute(query)

	# 3) Fetch the data into local variables as needed from the cursor, one row at a time.
	ans = crsr.fetchall() 

	print(Q)
	for i in range(len(ans)): 
		print ("\n\t{}. {} -- {}".format(i+1, ans[i][0], ans[i][1]))

	print ("\n")
	# 4) Close the cursor when done.
	connection.close()


get_ans(Q1, query1)
get_ans(Q2, query2)
get_ans(Q3, query3)
