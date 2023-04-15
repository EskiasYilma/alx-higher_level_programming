#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name_searched = sys.argv[4]

db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

cursor = db.cursor()

cursor.execute("SELECT * FROM states WHERE name='%s' ORDER BY id ASC" % state_name_searched)

results = cursor.fetchall()

for row in results:
    print(f"({row[0]}: {row[1]})")

db.close()
