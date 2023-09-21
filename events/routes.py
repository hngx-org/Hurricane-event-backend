from flask import Blueprint, abort, jsonify
import models  # storage will be used for all db session based queries
from models.user import User
from models.comment import Comment
from models.event import Event
# from models.interested_event import InterestedEvent
# Routes for handling event related functionality
# (event creation, updating and deleting)

"""This are the required imports do not change them and if you must import
something else be sure to specify it in your documentation reason you had to
import
"""

event_bp = Blueprint('events', __name__)

"""
    A GET Endpoint that returns a list of comments for an event
"""


@event_bp.route('/events/<event_id>/comments', methods=['GET'])
def retrieve_comments_by_event(event_id):
    try:
        all_comments = models.storage.all(Comment)
        comments = [
            comment for comment in all_comments if comment.event_id == event_id]
        return jsonify(
            {
                "event_id": event_id,
                'comments': [comment.json() for comment in comments]
            }
        )
    except Exception as e:
        models.storage.session.rollback()
        return jsonify({"error": e}), 404


# Create an Endpoint that GET's the images assiociated with a comment
@event_bp.route('/api/comments/<comment_id>/images', methods=['GET'])
def get_images_for_comment(comment_id):
    try:

        comment = models.storage.get(Comment, comment_id)

        if comment is None:
            return jsonify({"error": "Comment not found"}), 404

        comment_images = comment.images

        return jsonify({"comment_id": comment_id, "images": comment_images})

    except Exception as e:
        models.storage.session.rollback()
        return jsonify({"error": str(e)}), 404
