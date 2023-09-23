
# Routes for handling event related functionality (event creation, updating and deleting)

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request, abort
import re
from models import db, Event, GroupEvent

event = Blueprint('event', __name__)


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
=======

# Routes for handling event related functionality (event creation, updating and deleting)

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request, abort
import re
from models import db, Event, GroupEvent

event = Blueprint('event', __name__)


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

