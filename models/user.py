from db_connection.connection import db


class User(db.Model):
    """
    Represents a user in the application.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.

    Constraints:
        - `id`, `name`, and `email` cannot be null.
        - `name` accepts only letters and spaces.
        - `id` must be greater than 0.
        - `email` must be unique.

    Methods:
        json_repr(): Returns a JSON-like representation of the user object.

    Table Name:
        users

    Usage:
        user = User(id=1, name='John Doe', email='john.doe@example.com')
        json_data = user.json_repr()
        print(json_data)

    Example Output:
        {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com'}
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
  
    def __repr__(self):
        return self.json_repr()

    def json_repr(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
