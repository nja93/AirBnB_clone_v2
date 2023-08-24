#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Amenity(BaseModel, Base):
    '''class amenity'''
    __tablename__ = 'amenities'
    name =  Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity')

