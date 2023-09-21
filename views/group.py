import models
from . import api_views
from models.group import Group


@api_views.route("/groups", methods=["POST"])
def create_group():
    """Creates a new group"""
    pass


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
