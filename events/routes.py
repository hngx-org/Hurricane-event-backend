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


"""
    A DELETE Endpoint for deleting events belonging to a user by id. It also requires a 'userId'
"""
@event_bp.route('/events/<event_id:int>/<user_id:int>', methods=['DELETE'])
def delete_event(event_id, user_id):
    try:
        event_to_be_deleted = models.storage.get("Event", id=event_id, user_id=user_id)
        if event_to_be_deleted:
            event_to_be_deleted.delete()
            return jsonify({
                "success": True,
                "message": "Event was successfully deleted"
            })
        else:
            return jsonify({
                "success": False,
                "message": f"Could not delete event. No event with id -{event_id} belonging to user with id -{user_id} was found"
            })
    except Exception as e:
        models.storage.session.rollback()
        return jsonify({"error": e}), 404
>>>>>>> 27f6950b5a224899dbfc2a8df65bd34dc9cd08d3
