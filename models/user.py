"""Model of the User class"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base
from models.group import user_groups
from models.event import interested_events
from models.comment_likes import comment_likes


class User(BaseModel, Base):
    """User Class"""

    __tablename__ = "users"
    name = Column(String(120))
    email = Column(String(120), unique=True)
    avatar = Column(String(255), nullable=True)
    groups = relationship("Group", secondary=user_groups,
                          back_populates="users")
    events = relationship("Event", secondary=interested_events,
                          back_populates="users")
    liked_comments = relationship("Comment", secondary=comment_likes,
                                  back_populates="likes")

    def __init__(self, name: str, email: str, avatar: str):
        """Initializes the User class"""
        self.name = name
        self.email = email
        self.avatar = avatar

        super().__init__()

    # Serialize
    def serialize(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'avatar': self.avatar
        }
