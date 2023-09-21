import models
from . import api_views
from models.user import User


@api_views.route("/auth", methods=["POST"])
def authenticate_user():
    """Authenticates a user
    Returns: user_id
    """
    pass


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
