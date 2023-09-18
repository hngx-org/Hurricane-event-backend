from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

# Define a model(Test Purpose) 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   

# Create the database tables (you need to call this only once)
with app.app_context():
    db.create_all()

# This code initializes a Flask app, configures the SQLite database, creates a SQLAlchemy database instance,
# and defines a simple "User" model. The "SQLALCHEMY_DATABASE_URI" specifies the SQLite database file,
# and "SQLALCHEMY_TRACK_MODIFICATIONS" disables Flask-SQLAlchemy modification tracking to save resources.

# You can create models and modify the database as needed using the SQLAlchemy ORM.


