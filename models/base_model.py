#!/usr/bin/python3
from datetime import date
from uuid import uuid4
"""Defines the BaseModel class"""


class BaseModel:
    """Represent the BaseModel of the HBnB project."""

    def __init__ (self):
        """Initaialize a new BaseModel."""

        self.id = str(uuid4())
        self.created_at = date.today()
        self.updated_at = date.today()

    def __str__ (self):
        """return class name and id"""

        className = self.__class__.__name__
        return ("[{}] ({}) {}".format(className, self.id, self.__dict__))

