#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

env = environ.get('HBNB_TYPE_STORAGE')
if env == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
