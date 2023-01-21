#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            """getter function for cities"""
            state_list = []
            all_city = models.storage.all(City)
            for city in all_city.values():
                if city.state_id == self.id:
                    state_list.append(city)
            return state_list
