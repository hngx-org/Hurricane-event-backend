from db_connection.connection import db


class Comment(db.Model):
    """
    Comment model represents a comment on an event.

    Attributes:
        id (str): The unique identifier for the comment as a text-based UUID.
        body (str): Text content of the comment.
        user_id (str): The foreign key to the User model as a text-based UUID representing the comment's author.
        event_id (str): The foreign key to the Event model as a text-based UUID representing the event the comment is on.
    """
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  
    body = db.Column(db.String(255))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'))  
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'))  