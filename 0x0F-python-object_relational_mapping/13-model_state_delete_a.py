#!/usr/bin/python3
"""
A script that deletes all State objects with a \
name containing the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine, insert, update
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
    a = session.query(State).filter(State.name.contains('a'))
    a.delete(synchronize_session=False)
    session.commit()
    session.flush()
