"""Model for Images"""
from sqlalchemy import Column, String, ForeignKey
from models.basemodel import BaseModel, Base


class Image(BaseModel, Base):
    """Image class"""

    __tablename__ = "images"
    url = Column(String(255))

    def __init__(self, image_url: str):
        """Initializes the image object"""
        self.url = image_url

        super().__init__()
