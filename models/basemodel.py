"""Base Model of the application"""
from uuid import uuid4
from datetime import date, datetime
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """BaseModel Class"""

    id = Column(String(60), primary_key=True, default=str(uuid4()))

    def __init__(self):
        """Adds the object to a new session"""
        models.storage.new(self)

    def to_dict(self):
        """Converts object's properties to dict object

        Returns:
            dict: Dictionary representation of object
        """
        new_dict = self.__dict__.copy()

        if "_sa_instance_state" in new_dict:
            new_dict.pop("_sa_instance_state")
        for key, value in new_dict.items():
            if type(value) is date:
                new_dict[key] = value.isoformat()
            if type(value) is datetime:
                new_dict[key] = value.isoformat()

        return new_dict

    def save(self):
        """Saves the current state of the object"""
        models.storage.save()

    def delete(self):
        """Deletes itself from the session"""
        models.storage.obj_delete(self)

    def update(self, **kwargs):
        """Updates a field in the Model"""
        for key, value in kwargs.items():
            if key.endswith("date"):
                value = date.fromisoformat(kwargs[key])
            if key.endswith("time"):
                value = datetime.fromisoformat(kwargs[key])
            setattr(self, key, value)
