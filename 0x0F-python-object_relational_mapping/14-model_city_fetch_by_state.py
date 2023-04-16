#!/usr/bin/python3
"""
A script that prints all City objects from the database \
hbtn_0e_14_usa
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
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

    results = session.query(City, State).filter(
              City.state_id == State.id).order_by(City.id).all()
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
