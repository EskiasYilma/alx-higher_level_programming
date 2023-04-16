#!/usr/bin/python3
"""
A script that prints the State object with the name \
passed as argument from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine, text
    from model_state import Base, State
    import sys

    # if len(sys.argv) != 5:
    #     exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4].split("'")[0]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                               (mysql_username,
                                mysql_password,
                                database_name), pool_pre_ping=True)
    except Exception:
        exit(1)

    query = text("SELECT * FROM states WHERE name = :state_name")
    result = engine.execute(query, state_name=state_name_searched)

    row = result.fetchone()
    if row is not None:
        state_id = row['id']
        print(state_id)
    else:
        print("Not Found")
