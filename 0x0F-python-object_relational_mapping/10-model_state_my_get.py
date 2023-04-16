#!/usr/bin/python3
"""
A script that prints the State object with the name \
passed as argument from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv) != 5:
        exit(0)

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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).filter(
                  State.name == (state_name_searched,))

    if first_state.first() is None:
        print("Not Found")
    else:
        print(first_state[0].id)

    session.close()
