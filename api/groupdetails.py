from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace 'your_database_uri_here' with your actual database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'DBurl'
db = SQLAlchemy(app)

# Define the Group model (assuming you have a 'group' table in your database)
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(255))
    users = db.relationship('User', secondary='group_user', backref='groups')
    events = db.relationship('Event', backref='group')

# Define the User model (assuming you have a 'user' table in your database)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)

# Define the Event model (assuming you have an 'event' table in your database)
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

# Define the association table for User and Group (many-to-many relationship)
group_user = db.Table('group_user',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
)

# Create the database tables (moved out of the app context)
db.create_all()

# API endpoints

# Endpoint to create a new group
@app.route('/api/groups', methods=['POST'])
def create_group():
    data = request.get_json()
    name = data.get('name')
    img_url = data.get('img_url')

    if not name:
        return jsonify({'error': 'Group name is required'}), 400

    # Create a new group (replace with your logic)
    new_group = Group(name=name, img_url=img_url)
    db.session.add(new_group)
    db.session.commit()

    return jsonify({'message': 'Group created successfully'}), 201

# Endpoint to get group details
@app.route('/api/groups/<int:groupId>', methods=['GET'])
def get_group_details(groupId):
    group = Group.query.get(groupId)
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    # Retrieve user and event details
    users = [{'id': user.id, 'username': user.username} for user in group.users]
    events = [{'id': event.id, 'name': event.name, 'date': event.date} for event in group.events]

    group_details = {
        'name': group.name,
        'img_url': group.img_url,
        'users': users,
        'events': events
    }

    return jsonify(group_details), 200

if __name__ == '__main__':
    app.run(debug=True)
