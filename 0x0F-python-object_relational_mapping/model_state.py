#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base():
    using the module SQLAlchemy
    connect to a MySQL server running on
    localhost at port 3306
"""

from sqlalchemy.ext.declaritive import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class:
        - inherits from Base Tips
        - links to the MySQL table states
        - class attribute id that represents a column
        of an auto-generated, unique integer,
        - can’t be null and is a primary key
        - class attribute name that represents a column of a string
        with maximum 128 characters and can’t be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
