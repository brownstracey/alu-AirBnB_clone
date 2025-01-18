#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    name = ""
    state_id = ""
    """initialise class"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a City instance. If given, the arguments are used to set the
        instance's attributes. Otherwise, the instance's attributes are set to
        empty strings.
        """
        super().__init__(*args, **kwargs)