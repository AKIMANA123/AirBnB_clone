#!/usr/bin/python3
"""This module defines the BaseModel class."""
import models
from datetime import datetime
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_format))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update updated_at with the current datetime and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
