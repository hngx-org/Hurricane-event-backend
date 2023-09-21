from flask import Blueprint, request, jsonify
from models.group import Group  # Import the Group model
from models.user import User
import models

# Create a Blueprint for group-related routes
group_bp = Blueprint('groups', __name__)

# Route to create a new group
@group_bp.route('/groups', methods=['POST'])
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
        return jsonify(new_group.json()), 201
    except Exception as e:
        # Handle database errors
        models.storage.rollback()
        return jsonify({'error': str(e)}), 500

@group_bp.route('/groups/<groupId>', methods=['PUT'])
def update_group(groupId):
    '''This function updates the details of a
    group.

    Args: groupId, new_name of the group
    Returns the updated group details'''

    if request.json():
        data = request.json()
        title = data['title']
        group = models.storage.get('Group', groupId)
        group.title = title
        group.save()

        return jsonify(group.json())
    else:
        return jsonify({"Error", "Invalid parameters"}), 403

@group_bp.route('/groups/<userid>/groups', methods=['GET'])
def get_user_groups(userid):
    """Gets all the groups a user is part of

    Args:
        userid (str | uuid): The user I used to deterrmine which
        user groups are requested for

    Returns:
        JSON | str: Returns all the groups a user is part of
    """
    user = models.storage.get(User, userid)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    all_groups = models.storage.all(Group)
    groups = [group for group in all_groups if group.user_id == userid]
    group_list = [{'id': group.id, 'name': group.name} for group in groups]

    return jsonify({'user_id': userid, 'groups': group_list}), 200


@group_bp.route('/groups/<groupId>/members/<userId>', methods=['POST'])
def add_user_to_group(groupId, userId):
    user = models.storage.get(User, userId)
    group = models.storage.get(Group, groupId)

    if not group:
        return jsonify({'error: Group not found'}), 404
    if not user:
        return jsonify({'error': 'User not found'}), 404


    user_group = user_groups.insert().values(user_id=userId, group_id=groupId) # adding user[userId] to group[groupId]
    db.session.execute(user_group)
    db.session.commit()  

    return jsonify({'message': 'User added to group successfully'}), 200


@group_bp.route('/groups/<groupId>/members/<userId>', methods=['DELETE'])
def remove_user_from_group(groupId, userId):
    user = models.storage.get(User, userId)
    group = models.storage.get(Group, groupId)

    if not group:
        return jsonify({'error': 'Group not found'}), 404
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    user_group = user_groups.delete().where(
        user_groups.c.user_id == userId,
        user_groups.c.group_id == groupId
    )
    db.session.execute(user_group)
    db.session.commit()
    
    return jsonify({'message': 'User removed from the group successfully'}), 200              

