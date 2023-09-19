# Database connection script
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """declarative base"""
    pass

db = SQLAlchemy(model_class=Base)
