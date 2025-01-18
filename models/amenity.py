#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""
    """initialise class"""

    def __init__(self, *args, **kwargs):
        """
        Initialize an Amenity instance by inheriting from BaseModel.
        Accepts variable arguments and keyword arguments.
        """

        super().__init__(*args, **kwargs)