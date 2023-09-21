from flask import Flask, jsonify, request
from db_connection.db import db, Group

app = Flask(__name__)

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
