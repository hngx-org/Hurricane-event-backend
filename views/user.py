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
        users = models.search("User", email=email)
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
    pass


@api_views.route("/users/<user_id>", methods=["PUT"])
def update_profile(user_id):
    """Updates a user resource"""
    pass


@api_views.route("/users/<user_id>/interests/<event_id>",
                 methods=["POST"])
def express_interest(user_id, event_id):
    """Adds an event to user resource"""
    pass


@api_views.route("/users/<user_id>/interests/<event_id>",
                 methods=["DELETE"])
def remove_interest(user_id, event_id):
    """Removes an event from user resource"""
    pass
