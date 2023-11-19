#!/usr/bin/python3
"""
    sorts the results in ascending order by cities.id
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    query = """SELECT GROUP_CONCAT(cities.name ORDER BY cities.id SEPARATOR ASC ', ')
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s"""

    cursor.execute(query, (state_name,))

    result = cursor.fetchone()

    if result[0] is not None:
        print(result[0])

    cursor.close()
    db.close()
