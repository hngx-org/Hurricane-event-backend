from db_connection.connection import db

class Image(db.Model):
    """
    Image model represents an image associated with a comment.

    Attributes:
        id (str): The unique identifier for the image as a text-based UUID.
        comment_id (str): The foreign key to the Comment model as a text-based UUID representing the comment the image is associated with.
        image_url (str): URL to the image.
    """
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  
    comment_id = db.Column(db.String(36), db.ForeignKey('comment.id'))  
    image_url = db.Column(db.String(255))
