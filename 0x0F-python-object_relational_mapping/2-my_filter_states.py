#!/usr/bin/python3
"""
A script that takes in an argument and displays \
all values in the states table of hbtn_0e_0_usa \
where name matches the argument.
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
    my_query = "SELECT id, name FROM states WHERE name = '{}' \
                ORDER BY id ASC".format(state_name_searched)
    cursor.execute(my_query)

    results = cursor.fetchall()

    for row in results:
        if row[1] == state_name_searched:
            print(row)

    db.close()
