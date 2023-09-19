from db_connection.connection import db


class GroupEvent(db.Model):
    """
    GroupEvent model represents the relationship between groups and events.

    Attributes:
        event_id (str): The foreign key to the Event model as a text-based UUID.
        group_id (str): The foreign key to the Group model as a text-based UUID.
    """
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'), primary_key=True)  
    group_id = db.Column(db.String(36), db.ForeignKey('group.id'), primary_key=True)  
