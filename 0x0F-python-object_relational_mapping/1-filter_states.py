#!/usr/bin/python3
"""
    lists all states with a name starting with N (upper N) from the database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    # Execute the SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetch all rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
