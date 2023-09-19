"""Model for Comment table"""
from sqlalchemy import Column, String, ForeignKey
from models.basemodel import BaseModel, Base


class Comment(BaseModel, Base):
    """Comment Class"""

    __tablename__ = "comments"
    body = Column(String(1024))
    user_id = Column(String(60), ForeignKey("users.id"))
    event_id = Column(String(60), ForeignKey("events.id"))

    def __init__(self, body: str, user_id: str, event_id: str):
        """Initialized the comment"""
        self.body = body
        self.user_id = user_id
        self.event_id = event_id
