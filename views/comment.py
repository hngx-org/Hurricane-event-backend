import models
from . import api_views
from models.event import Event
from models.comment import Comment


@api_views.route("/events/<event_id>/comments", methods=["POST"])
def add_comment(event_id):
    """Adds a comment to an event"""
    pass


@api_views.route("/events/<event_id>/comments")
def get_comment(event_id):
    """Gets comments of an event"""
    pass


@api_views.route("/comments/<comment_id>/images", methods=["POST"])
def add_comment_img(comment_id):
    """Adds an image to a comment"""
    pass


@api_views.route("/comments/<comment_id>/images")
def remove_comment_img(comment_id):
    """Removes an image from comments"""
    pass
