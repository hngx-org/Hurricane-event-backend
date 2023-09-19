"""Init file for models"""
from .engine.database import DBStorage

storage = DBStorage()
storage.load()
