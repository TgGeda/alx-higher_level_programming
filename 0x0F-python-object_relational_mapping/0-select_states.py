#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""
import MySQLdb
import sys

def retrieve_all_states(username, password, dbname):
    # Connect to MySQL server
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=username, passwd=password, db=dbname)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Retrieve the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Call the function to retrieve and display all states
    retrieve_all_states(username, password, dbname)
