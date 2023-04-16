#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from relationship_state import Base, State
    from relationship_city import City
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

    all_states = session.query(State).order_by(State.id).all()
    for state in all_states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
