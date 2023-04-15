#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
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
    first_state = session.query(State).first()

    print("{}: {}".format(first_state.id, first_state.name)
          if first_state is not None else "Nothing")

    session.close()
