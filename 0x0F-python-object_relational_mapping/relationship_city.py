#!/usr/bin/python3

"""
class definition of a City and an instance Base \
    from model_state
    using the module SQLAlchemy
    connect to a MySQL server running on
    localhost at port 3306
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    City class:
        - inherits from Base (imported from model_state)
        - links to the MySQL table cities
        - class attribute id that represents a column of an \
        auto-generated, unique integer, can’t be null and is \
        a primary key
        - class attribute name that represents a column of a \
        string of 128 characters and can’t be null
        - class attribute state_id that represents a column \
        of an integer, can’t be null and is a foreign key to states.id
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
