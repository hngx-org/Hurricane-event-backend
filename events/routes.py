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
        return jsonify({'message': 'Event not found'}), 401
    
    data = request.get_json()
    event.title = data.get('title', event.title)
    event.description = data.get('description', event.description)
    event.location = data.get('locaton', event.location)
    event.start_time = datetime.strptime(data.get('start_time'), '%Y-%m-%d %H:%M:%S') if data.get('start_time') else event.start_time
    event.end_time = datetime.strptime(data.get('end_time'), '%Y-%m-%d %H:%M:%S') if data.get('end_time') else event.end_time


    models.storage.commit()
    return jsonify({'message': 'Event updated successfully'}), 200


    
