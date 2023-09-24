from flask import Blueprint, abort, jsonify, request
import models # storage will be used for all db session based queries
from models.user import User
from models.comment import Comment
from models.event import Event
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
import re
from models import db, Event, GroupEvent
# from models.interested_event import InterestedEvent
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
"""
    An Enpoint for updating users events
"""
@event.route('/events/<event_id>', method=['PUT'])
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
""" 
    A DELETE Endpoint for deleting events belonging to a user by id. It also requires a 'userId'
"""
@event.route('/events/<event_id:int>/<user_id:int>', methods=['DELETE'])
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

# Function to validate image URL
def validate_image_url(url):
    # Define a regex pattern for a valid image URL
    url_pattern = r'^(https?://)?(www\.)?[\w.-]+\.[a-zA-Z]{2,}(?:/[\w.-]*)*/?$'
    
    return re.match(url_pattern, url) is not None


@event.route('/api/events', methods=['POST'])
@jwt_required()
def create_event():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    location = data.get('location')
    start_date = data.get('start_date')
    start_time = data.get('start_time')
    end_date = data.get('end_date')
    end_time = data.get('end_time')
    thumbnail = data.get('thumbnail')
    group_id = data.get('group_id')


    current_user_id = get_jwt_identity()

    if not validate_image_url(thumbnail):
        return jsonify(message='Invalid thumbnail image URL'), 400

    
    
    # Create a new event
    event = Event(
        title=title,
        description=description,
        location=location,
        start_date=start_date,
        start_time=start_time,
        end_date=end_date,
        end_time=end_time,
        thumbnail_url=thumbnail,
        user_id=current_user_id,
    )

    db.session.add(event)
    db.session.commit()

    group_event = GroupEvent(event_id=event.id, group_id=group_id)

    db.session.add(group_event)
    db.session.commit()

    return jsonify({'message': 'Event successfully added'}), 201

