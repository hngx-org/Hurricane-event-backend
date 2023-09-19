from db_connection.connection import db


class Event(db.Model):
    """
    Event model represents an event in the system.

    Attributes:
        id (str): The unique identifier for the event as a text-based UUID.
        title (str): The title or name of the event.
        description (str): A description of the event.
        creator (str): The foreign key to the User model as a text-based UUID representing the event's creator.
        location (str): The location of the event.
        start_date (date): The date when the event starts.
        end_date (date): The date when the event ends.
        start_time (timestamp): The timestamp when the event starts.
        end_time (timestamp): The timestamp when the event ends.
        thumbnail (str): URL to the event's thumbnail image.
    """
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    creator = db.Column(db.String(36), db.ForeignKey('user.id')) 
    location = db.Column(db.String(255))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    start_time = db.Column(db.TIMESTAMP)
    end_time = db.Column(db.TIMESTAMP)
    thumbnail = db.Column(db.String(255))
