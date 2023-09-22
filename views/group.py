from flask import request, jsonify
import models
from . import api_views
from models.group import Group


@api_views.route("/groups", methods=["POST"])
def create_group():
    """Creates a new group"""
    data = request.get_json()
    title = data.get("title")

    # Check if 'title' is provided in the JSON data
    if not title:
        return jsonify({'message': 'Title is required'}), 412

    all_groups = models.storage.all(Group)

    title_exists = [group for group in all_groups if group.title == title]

    if title_exists:
        return jsonify({'message': 'Group already exists'})

    # Create a new group instance
    new_group = Group(title=title)
    # Commit the changes to the database
    new_group.save()
    return jsonify(new_group.to_dict()), 201


@api_views.route("/groups/<group_id>")
def get_group(group_id):
    """Gets a group resource"""
    group = models.storage.get('Group', group_id)

    if not group:
        return jsonify({"message": "Group not found"}), 404

    return jsonify(group.to_dict()), 200


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
