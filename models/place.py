#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews= relationship('Review', cascade='all, delete, delete-orphan', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, back_populates='place_amenities')

'''if not set to db, defines property rev'''
    else:
    @property
    def reviews(self):
        from models import storage
        rev_instances = storage.all("Review").values()
        return [review for review in rev_instances

    if review.place_id == self.id]
    
        @property
        def amenities(self):
            from models import storage
            amenity_instances = storage.all("Amenity").values()
            return [amenity for amenity in amenity_instances
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj)
