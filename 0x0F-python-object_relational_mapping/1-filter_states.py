#!/usr/bin/python3
"""
A script that lists all states with a name \
starting with N (upper N) from the database hbtn_0e_0_usa
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

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(f"({row[0]}, '{row[1]}')")

    db.close()
