#!/usr/bin/python3
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
import models
"""This module defines a class to manage sqlachemy for hbnb clone"""


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = environ.get('HBNB_MYSQL_USER')
        pas = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = environ.get('HBNB_MYSQL_DB')
        env = environ.get('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pas, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
            # engine specify database connection where operations are perfomed

    def all(self, cls=None):
        my_classes = [User, State, City, Amenity, Place, Review]
        dictionary = {}
        if cls is not None:
            for value in self.__session.query(cls):
                key = '{}.{}'.format(value.__class__.__name__, value.id)
                dictionary[key] = value
        else:
            for clas in my_classes:
                for value in self.__session.query(clas):
                    key = '{}.{}'.format(value.__class__.__name__, value.id)
                    dictionary[key] = value
        return dictionary

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            Base.metadata.drop_all(self.__engine)
            # Deleting a database is basically dropping all the tables

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Var_Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Var_Session)
        self.__session = Session()
