#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and \
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name)

    cursor = db.cursor()
    my_query = "SELECT cities.name FROM states INNER \
                JOIN cities ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC"
    cursor.execute(my_query, (state_name_searched,))

    results = cursor.fetchall()

    print(", ".join([row[0] for row in results]))

    db.close()
