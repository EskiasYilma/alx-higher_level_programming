#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys
    from sqlalchemy.orm import sessionmaker

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (mysql_username,
                            mysql_password,
                            database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State)

    for i in first_state:
        if "a" in str(i.name):
            print("{}: {}".format(i.id, i.name))

    session.close()
