from db_connection.connection import db

class Group(db.Model):
    """
    Group model represents a group or community in the system.

    Attributes:
        id (str): The unique identifier for the group as a text-based UUID.
        title (str): The title or name of the group.
    """
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  
    title = db.Column(db.String(255))
