from flask import Blueprint, abort, jsonify, request
import models # storage will be used for all db session based queries
from models.user import User
from models.comment import Comment
from models.event import Event
from datetime import datetime
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
"""
    An Enpoint for updating users events
"""
@event_bp.route('/events/<event_id>', method=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'Event not found'}), 404
    
    try:
        data = request.get_json()
        event.update(**data)
        models.storage.session.commit()
        return jsonify({'message': 'Event updated successfully'}), 200
    except Exception as e:
        # Rollback the session in case of an error
        models.storage.session.rollback()
        return jsonify({"error": str(e)}), 400
    

    
