"""Model for Images"""
from sqlalchemy import Column, String, ForeignKey
from models.basemodel import BaseModel, Base


class Image(BaseModel, Base):
    """Image class"""

    __tablename__ = "images"
    image_url = Column(String(255))
    comment_id = Column(String(60), ForeignKey("comments.id"))

    def __init__(self, image_url: str, comment_id: str):
        """Initializes the image object"""
        self.image_url = image_url
        self.comment_id = comment_id

        super().__init__()
