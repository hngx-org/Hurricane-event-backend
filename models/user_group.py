from db_connection.connection import db


class UserGroup(db.Model):
    """
    UserGroup model represents the relationship between users and groups.

    Attributes:
        user_id (str): The foreign key to the User model as a text-based UUID.
        group_id (str): The foreign key to the Group model as a text-based UUID.
    """
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), primary_key=True) 
    group_id = db.Column(db.String(36), db.ForeignKey('group.id'), primary_key=True) 
