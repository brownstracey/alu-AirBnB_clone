#!/usr/bin/python3
"""
Module for the BaseModel class.
"""


import uuid
from datetime import datetime


class BaseModel:
    """Defines common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """initialize the data model"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                elif key != "__class__":
                    setattr(self, key, value)


    def __str__(self):
        """Return string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """Update the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()


    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        # Copy __dict__ and add `__class__` key
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        # Convert datetime attributes to ISO format
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
    