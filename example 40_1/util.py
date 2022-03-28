import psycopg2
from psycopg2 import Error

# this function is based on the tutorial at: https://pynative.com/python-postgresql-tutorial/
def connect_to_db(username='raywu1990',password='test',host='127.0.0.1',port='5432',database='dvdrental'):
	try:
	    # Connect to an existing database
	    connection = psycopg2.connect(user=username,
	                                  password=password,
	                                  host=host,
	                                  port=port,
	                                  database=database)

	    # Create a cursor to perform database operations
	    cursor = connection.cursor()
	    print("connected to the database")

	    return cursor, connection

	except (Exception, Error) as error:
	    print("Error while connecting to PostgreSQL", error)
	

def disconnect_from_db(connection,cursor):
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
    	print("Connection does not work.")



# run_sql(cursor,"select from;")
def run_and_fetch_sql(cursor, sql_string=""):
	try:
	    # Executing a SQL query
	    # cursor.execute("SELECT version();")
	    # cursor.execute("SELECT * from customer;")
	    cursor.execute(sql_string)
	    # Fetch result
	    # record = cursor.fetchone()
	    # print("You are connected to - ", record, "\n")
	    record = cursor.fetchall()
	    # print("Here are the first 5 rows", record[:5])
	    return record
	except (Exception, Error) as error:
		print("Errors while executes the code: ", error)
		return -1