"""Model for Comment table"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base
from models.comment_image import comment_image
from models.comment_likes import comment_likes


class Comment(BaseModel, Base):
    """Comment Class"""

    __tablename__ = "comments"
    body = Column(String(1024))
    user_id = Column(String(60), ForeignKey("users.id"))
    event_id = Column(String(60), ForeignKey("events.id"))
    image = relationship("Image", secondary=comment_image, uselist=False)
    likes = relationship("User", secondary=comment_likes,
                         back_populates="liked_comments")

    def __init__(self, body: str, user_id: str, event_id: str):
        """Initialized the comment"""
        self.body = body
        self.user_id = user_id
        self.event_id = event_id

        super().__init__()

    # formatter for the comment class
    def json(self):
        return {
            'id': self.id,
            'body': self.body,
            'event_id': self.event_id
            }
