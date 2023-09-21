from flask import Blueprint, abort, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import models # storage will be used for all db session based queries
from models.user import User
from models.comment import Comment
from models.event import Event
from models.interested_event import InterestedEvent
# Routes for handling event related functionality
# (event creation, updating and deleting)

"""This are the required imports do not change them and if you must import
something else be sure to specify it in your documentation reason you had to
import
"""

event = Blueprint('events', __name__)

"""
    A GET Endpoint that returns a list of comments for an event
"""
@event.route('/events/<event_id>/comments', methods=['GET'])
def retrieve_comments_by_event(event_id):
    try:
        all_comments = models.storage.all(Comment)
        comments = [comment for comment in all_comments if comment.event_id == event_id]
        return jsonify(
                {
                    "event_id": event_id,
                    'comments': [comment.json() for comment in comments]
                    }
                )
    except Exception as e:
        models.storage.session.rollback()
        return jsonify({"error": e}), 404

comment_likes_bp = Blueprint('comment_likes', __name__)

"""
    A POST Endpoint that adds a like to a comment
"""
@comment_likes_bp.route('/api/<int:comment_id>/<string:user_id>/likes', methods=['POST'])
@jwt_required
def add_like_to_comment(comment_id, user_id):
    comment = Comment.query.get(comment_id)

    # Check if the comment exists
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    # Check if the user has already liked the comment
    if user_id in comment.likes:
        return jsonify({"error": "User has already liked this comment"}), 400

    try:
        # Append the user_id to the comment's likes and save
        comment.likes.append(user_id)
        models.storage.save()

        return jsonify(
            {
                'success': True,
                'comment_id': comment.id,
                'likes': comment.likes
            }
        )
    except Exception as e:
        models.storage.session.rollback()
        return jsonify({"error": str(e)}), 500