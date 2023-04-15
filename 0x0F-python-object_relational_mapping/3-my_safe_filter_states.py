#!/usr/bin/python3
"""
A script that takes in arguments and displays \
all values in the states table of hbtn_0e_0_usa\
 where name matches the argument. But this time,\
 write one that is safe from MySQL injections!
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

    cursor.execute("SELECT * FROM states WHERE name = %(search)s \
                    ORDER BY id ASC", {'search': state_name_searched})

    results = cursor.fetchall()

    for row in results:
        print(f"({row[0]}, '{row[1]}')")

    db.close()
