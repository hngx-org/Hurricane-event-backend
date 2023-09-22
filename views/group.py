from flask import request, jsonify
import models
from . import api_views
from models.group import Group


@api_views.route("/groups", methods=["POST"])
def create_group():
    """Creates a new group"""
    data = request.get_json()
    title = data.get("title")
    image = data.get("image")

    # Check if 'title' is provided in the JSON data
    if not title:
        return jsonify({'message': 'Title is required'}), 412

    all_groups = models.storage.all(Group)

    title_exists = [group for group in all_groups if group.title == title]

    if title_exists:
        return jsonify({'message': 'Group already exists'})

    # Create a new group instance
    new_group = Group(title=title)
    if image:
        new_group.update(image=image)
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


@api_views.route("/groups/<group_id>", methods=["PUT"])
def update_group(group_id):
    """Updates a group resource"""
    data = request.get_json()
    title = data.get("title")
    image = data.get("image")

    group = models.storage.get("Group", group_id)
    if group:
        kwargs = {}
        if title:
            kwargs["title"] = title
        if image:
            kwargs["image"] = image
        if kwargs:
            group.update(**kwargs)
            group.save()
            return jsonify({"message": "success"}), 202
        return jsonify({"message": "unchanged"})
    return jsonify({"message": "Invalid Group ID"}), 404


@api_views.route("/groups/<group_id>", methods=["DELETE"])
def delete_group(group_id):
    """Deletes a group resource"""
    group = models.storage.get("Group", group_id)
    if group:
        models.storage.delete("Group", group_id)
        models.storage.save()
        return jsonify({"message": "success"})
    return jsonify({"message": "Invalid Group ID"}), 404


@api_views.route("/groups/<group_id>/members/<user_id>", methods=["POST"])
def add_user(group_id, user_id):
    """Adds a user to the group"""
    group = models.storage.get("Group", group_id)
    user = models.storage.get("User", user_id)

    if not user:
        return jsonify({"message": "Invalid User ID"}), 404
    if not group:
        return jsonify({"message": "Invalid Group ID"}), 404
    if user not in group.users:
        group.users.append(user)
        group.save()
    return jsonify({"message": "success"})


@api_views.route("/groups/<group_id>/members/<user_id>", methods=["DELETE"])
def remove_user(group_id, user_id):
    """Removes a user from group"""
    group = models.storage.get("Group", group_id)
    user = models.storage.get("User", user_id)

    if not user:
        return jsonify({"message": "Invalid User ID"}), 404
    if not group:
        return jsonify({"message": "Invalid Group ID"}), 404
    if user in group.users:
        group.users.remove(user)
        group.save()
    return jsonify({"message": "success"})
