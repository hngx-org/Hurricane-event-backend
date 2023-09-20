"""Model of the User class"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base
from models.group import user_groups
from models.event import interested_events


class User(BaseModel, Base):
    """User Class"""

    __tablename__ = "users"
    name = Column(String(120))
    email = Column(String(120), unique=True)
    access_token = Column(String(255))
    refresh_token = Column(String(255))
    avatar = Column(String(255), nullable=True)
    groups = relationship("Group", secondary=user_groups,
                          back_populates="users")
    events = relationship("Event", secondary=interested_events,
                          back_populates="users")

    def __init__(self, name: str, email: str, access_token: str,
                 refresh_token: str, avatar: str):
        """Initializes the User class"""
        self.name = name
        self.email = email
        self. access_token = access_token
        self.refresh_token = refresh_token
        self.avatar = avatar

        super().__init__()