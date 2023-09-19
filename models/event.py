from db_connection.connection import db
import uuid


class Event(db.Model):
    """
    Represents an event in the application.

    Attributes:
        id (str): Unique identifier for the event (UUID).
        title (str): Title of the event.
        description (str): Description of the event.
        creator (UserModel): Relationship to the UserModel representing the event creator.
        creator_id (str): ID of the user who created the event (references Users table).
        location (str): Location of the event.
        start_date (date): Start date of the event (format: 'YYYY-MM-DD').
        end_date (date): End date of the event (format: 'YYYY-MM-DD').
        start_time (time): Start time of the event (format: 'HH:MM:SS').
        end_time (time): End time of the event (format: 'HH:MM:SS').
        thumbnail (str): URL to the event's thumbnail image.

    Constraints:
        - `id`, `title`, `description`, `creator_id`, `location`, `start_date`, `end_date`, `start_time`, `end_time`, and `thumbnail` cannot be null.

    Usage:
        - To create a new event, instantiate EventModel and add it to the database.
        - To fetch event details, query the EventModel by its unique ID or other criteria.
        - To update an event, retrieve it from the database, modify its attributes, and save it.
        - To delete an event, retrieve it and delete it from the database.

    Example:
        {
           title="Sample Event",
            description="This is a sample event description.",
            creator_id="f47ac10b-58cc-4372-a567-0e02b2c3d479", 
            location="Sample Location",
            start_date="2023-09-20",
            end_date="2023-09-20",
            start_time="10:00:00",
            end_time="12:00:00",
            thumbnail="https://example.com/thumbnail.jpg",
        }

    """
    __tablename__ = "events"

    id = db.Column(db.String(60), default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    creator = db.relationship("User", backref="events")
    creator_id = db.Column(db.String(60), db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    location = db.Column(db.String(1024), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    thumbnail = db.Column(db.String(255), nullable=False)
    
