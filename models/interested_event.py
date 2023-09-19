from db_connection.connection import db

class InterestedEvent(db.Model):
    """
    InterestedEvent model represents the relationship between users and events they are interested in.

    Attributes:
        user_id (str): The foreign key to the User model as a text-based UUID.
        event_id (str): The foreign key to the Event model as a text-based UUID.
    """
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), primary_key=True)  
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'), primary_key=True) 
