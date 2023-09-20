# Routes for handling event related functionality (event creation, updating and deleting)
from flask import Blueprint
from db_connection.connection import db
from models.event import Event

event_route = Blueprint('event_route', __name__)

@event_route.route('/event/<event_id:int>/<user_id:int>', methods=['DELETE'])
def delete_event(event_id, user_id):
    event_to_be_deleted = Event.query.filter_by(id=event_id, creator_id=user_id).first()
    if event_to_be_deleted:
        db.session.delete(event_to_be_deleted)
        db.session.commit()