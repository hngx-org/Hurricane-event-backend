from flask import Blueprint, request, jsonify
from models.group import Group  # Import the Group model
import models

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

    try:
        # Commit the changes to the database
        new_group.save()
        response_data = {'id': new_group.id, 'title': new_group.title}
        return jsonify(response_data), 201
    except Exception as e:
        # Handle database errors
        models.storage.rollback()
        return jsonify({'error': str(e)}), 500

@group_bp.route('/api/groups/<groupId>', methods=['PUT'])
def update_group(groupId):
    '''This function updates the details of a
    group.

    Args: groupId
    Returns the updated group details'''

    if request.json():
        data = request.json()
        title = data['title']
        group = models.storage.get('Group', groupId)
        group.title = title
        group.save()

    return jsonify(group.json())
