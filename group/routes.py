from flask import Blueprint, request, jsonify
from models.group import Group  # Import the Group model
from db_connection.connection import db

# Create a Blueprint for group-related routes
group_bp = Blueprint('group', __name__)

# Route to create a new group
@group_bp.route('/api/groups', methods=['POST'])
def create_group():
    data = request.get_json()

    # Check if 'title' is provided in the JSON data
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    title = data['title']

    # Create a new group instance
    new_group = Group(title=title)

    # Add the new group to the database session
    db.session.add(new_group)

    try:
        # Commit the changes to the database
        db.session.commit()
        response_data = {'id': new_group.id, 'title': new_group.title}
        return jsonify(response_data), 201
    except Exception as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
