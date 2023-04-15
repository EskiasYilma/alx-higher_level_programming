#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name)

    cursor = db.cursor()
    my_query = "SELECT cities.id, cities.name, states.name FROM cities, \
                states WHERE cities.state_id = states.id GROUP BY cities.name \
                ORDER BY cities.id ASC"
    cursor.execute(my_query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()
