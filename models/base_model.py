#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
"""Defines the BaseModel class"""


class BaseModel:
    """Represent the BaseModel of the HBnB project."""

    def __init__ (self, *args, **kwargs):
        """Initaialize a new BaseModel."""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                r = self.__dict__
                if key == "created_at" or "updated_at":
                    value = datetime.now()
                    r["{}".format(key)] = value.isoformat
                r = self.__dict__
                r["{}".format(key)] = value
                

    def save(self):
        """update updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representaion of the BaseModel"""
        dict = self.__dict__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict

    def __str__ (self):
        """return class name and id"""

        className = self.__class__.__name__
        return ("[{}] ({}) {}".format(className, self.id, self.__dict__))

