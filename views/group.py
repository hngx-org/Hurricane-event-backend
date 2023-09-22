from flask import request, jsonify
import models
from . import api_views
from models.group import Group


@api_views.route("/groups", methods=["POST"])
def create_group():
    """Creates a new group"""
    data = request.get_json()

    # Check if 'title' is provided in the JSON data
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    title = data['title']

    all_groups = models.storage.all(Group)

    title_exists = [group for group in all_groups if group.title == title]

    if title_exists:
        return jsonify({'error': 'Title already exists'}) 

    # Add the new group to the database session

    try:
        # Create a new group instance
        new_group = Group(title=title)
        # Commit the changes to the database
        new_group.save()
        return jsonify(new_group.to_dict()), 201
    except Exception as e:
        # Handle database errors
        # models.storage.rollback()
        return jsonify({'error': str(e)}), 500


@api_views.route("/groups/<group_id>")
def get_group(group_id):
    """Gets a group resource"""
    pass


@api_views.route("/groups/<group_id>")
def update_group(group_id):
    """Updates a group resource"""
    pass


@api_views.route("/groups/<group_id>")
def delete_group(group_id):
    """Deletes a group resource"""
    pass


@api_views.route("/groups/<group_id>/members/<user_id>", methods=["POST"])
def add_user(group_id, user_id):
    """Adds a user to the group"""
    pass


@api_views.route("/groups/<group_id>/members/<user_id>", methods=["DELETE"])
def remove_user(group_id, user_id):
    """Removes a user from group"""
    pass
