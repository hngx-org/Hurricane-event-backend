import models
from . import api_views
from models.user import User
from flask import request, jsonify


@api_views.route("/auth", methods=["POST"])
def authenticate_user():
    """Authenticates a user
    Returns: user_id
    """
    data = request.get_json()
    email = data.get("email")
    name = data.get("name")
    avatar = data.get("avatar")

    if email:
        users = models.storage.search("User", email=email)
        if users:
            user = users[0]
        else:
            if name:
                user = User(name, email, avatar)
                user.save()
            else:
                return jsonify({"message": "No name found"}), 412
        return jsonify({"user_id": user.id})
    return jsonify({"message": "No email found"}), 412


@api_views.route("/users/<user_id>")
def get_profile(user_id):
    """Returns a user resource"""
    user = models.storage.get("User", user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"message": "User ID does not exist"}), 404


@api_views.route("/users/<user_id>", methods=["PUT"])
def update_profile(user_id):
    """Updates a user resource"""
    user = models.storage.get("User", user_id)
    if user:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        avatar = data.get("avatar")

        kwargs = {"name": name, "email": email, "avatar": avatar}
        for key, value in kwargs.copy().items():
            if not value:
                kwargs.pop(key)
        if kwargs:
            user.update(**kwargs)
            user.save()
            return jsonify({"message": "Update was successful"}), 202
        return jsonify({"message": "Unchanged"}), 200
    return jsonify({"message": "User ID does not exist"}), 404


@api_views.route("/users/<user_id>/interests/<event_id>",
                 methods=["POST"])
def express_interest(user_id, event_id):
    """Adds an event to user resource"""
    user = models.storage.get("User", user_id)
    event = models.storage.get("Event", event_id)
    if not user:
        return jsonify({"message": "Invalid User ID"}), 404
    if not event:
        return jsonify({"message": "Invalid Event ID"}), 404

    if event not in user.events:
        user.events.append(event)
        user.save()
    return jsonify({"message": "success"})


@api_views.route("/users/<user_id>/interests/<event_id>",
                 methods=["DELETE"])
def remove_interest(user_id, event_id):
    """Removes an event from user resource"""
    user = models.storage.get("User", user_id)
    event = models.storage.get("Event", event_id)
    if not user:
        return jsonify({"message": "Invalid User ID"}), 404
    if not event:
        return jsonify({"message": "Invalid Event ID"}), 404

    if event in user.events:
        user.events.remove(event)
        user.save()
    return jsonify({"message": "success"})


@api_views.route("/users/<user_id>/groups/<group_id>", methods=["POST"])
def invite_users(user_id, group_id):
    """Invites users to a group"""
    main_user = models.storage.get("User", user_id)
    group = models.storage.get("Group", group_id)

    if not main_user:
        return jsonify({"message": "Invalid User ID"}), 404
    if not group:
        return jsonify({"message": "Invalid Group ID"}), 404

    data = request.get_json()
    users = data.get("users")

    if not users:
        return jsonify({"message": "Users must be passed"}), 412

    added_users = []
    invalid_users = []

    for identity in users:
        user = models.storage.search("User", email=identity)
        if user:
            user = user[0]
            if user not in group.users:
                group.users.append(user)
            added_users.append(identity)
        else:
            invalid_users.append(identity)
    group.save()

    return jsonify({"message": "success",
                    "added_users": added_users,
                    "invalid_users": invalid_users})
