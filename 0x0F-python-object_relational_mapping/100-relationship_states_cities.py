#!/usr/bin/python3
"""
A Script that creates the State “California” with the City “San Francisco” \
from the database hbtn_0e_100_usa
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (mysql_username,
                            mysql_password,
                            database_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    add_state = State(name="California")
    add_city = City(name="San Francisco", state=add_state)

    session.add(add_state)
    session.add(add_city)
    session.commit()

    session.close()
