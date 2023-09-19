from flask_sqlalchemy import SQLAlchemy
import uuid 

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    """
    User model represents a user in the system.

    Attributes:
        id (str): The unique identifier for the user as a text-based UUID.
        name (str): The user's name.
        email (str): The user's email address.
        avatar (str): URL to the user's avatar.
    """
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    avatar = db.Column(db.String(255))

class Group(db.Model):
    __tablename__ = "groups"

    """
    Group model represents a group or community in the system.

    Attributes:
        id (str): The unique identifier for the group as a text-based UUID.
        title (str): The title or name of the group.
    """
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  
    title = db.Column(db.String(255))

class UserGroup(db.Model):
    __tablename__ = "user_groups"

    """
    UserGroup model represents the relationship between users and groups.

    Attributes:
        user_id (str): The foreign key to the User model as a text-based UUID.
        group_id (str): The foreign key to the Group model as a text-based UUID.
    """
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), primary_key=True) 
    group_id = db.Column(db.String(36), db.ForeignKey('group.id'), primary_key=True) 

class Event(db.Model):
    __tablename__ = "events"

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

class GroupEvent(db.Model):
    __tablename__ = "group_events"

    """
    GroupEvent model represents the relationship between groups and events.

    Attributes:
        event_id (str): The foreign key to the Event model as a text-based UUID.
        group_id (str): The foreign key to the Group model as a text-based UUID.
    """
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'), primary_key=True)  
    group_id = db.Column(db.String(36), db.ForeignKey('group.id'), primary_key=True)  

class InterestedEvent(db.Model):
    __tablename__ = "interested_events"

    """
    InterestedEvent model represents the relationship between users and events they are interested in.

    Attributes:
        user_id (str): The foreign key to the User model as a text-based UUID.
        event_id (str): The foreign key to the Event model as a text-based UUID.
    """
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), primary_key=True)  
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'), primary_key=True) 

class Comment(db.Model):
    __tablename__ = "comments"

    """
    Comment model represents a comment on an event.

    Attributes:
        id (str): The unique identifier for the comment as a text-based UUID.
        body (str): Text content of the comment.
        user_id (str): The foreign key to the User model as a text-based UUID representing the comment's author.
        event_id (str): The foreign key to the Event model as a text-based UUID representing the event the comment is on.
        image (relationship): it creates the link between comment and image
    """
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  
    body = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)  
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'), nullable=False)
    image = db.relationship("Image", back_populates="comment", lazy="dynamic")  

class Image(db.Model):
    __tablename__ = "images"

    """
    Image model represents an image associated with a comment.

    Attributes:
        id (str): The unique identifier for the image as a text-based UUID.
        comment_id (str): The foreign key to the Comment model as a text-based UUID representing the comment the image is associated with.
        image_url (str): URL to the image.
        comment (relationship): it creates the link between comment and image
    """
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  
    comment_id = db.Column(db.String(36), db.ForeignKey('comments.id'), nullable=False)
    comment = db.relationship("Comment", back_populates="image")  
    image_url = db.Column(db.String(255))

def init_db(app):
    """
    Initializes the database with the provided Flask app instance.

    Args:
        app: The Flask app instance.
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()

