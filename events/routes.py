import models# storage will be used for all db session based queries
from flask import Flask, Blueprint, jsonify, request
from models.user import User
from models.comment import Comment
from models.event import Event
from models.interested_event import InterestedEvent


# Routes for handling event related functionality (event creation, updating and deleting)

event = Blueprint('event', __name__)

# Route that adds a comment to an event
@event.route('/api/events/<int:event_id>/comments', methods=['POST'])
def add_comment(event_id):
        # Find the event
        event = Comment.query.filter(Comment.event_id == event_id).all()
        if not event:
            return jsonify({'message': 'Event does not exist'}), 404

        # Validate request body
        body = request.json.get('body')
        if not body:
            return jsonify({'message': 'Comment is required'}), 400
    try:
        # Create new comment object
        new_comment = Comment(id=user_id, body=body, event_id=event_id)

        # Add comment to the event
        event.comments.append(new_comment)

        # Save changes to the database
        models.storage.add(new_comment)
        models.storage.session.commit()

        # Return success response with the newly created comment
        return jsonify({'message': 'Comment added successfully'}), 201
        
    except SQLAlchemyError as e:
        models.storage.session.rollback()
        return jsonify({'message': 'Failed to add comment'}), 500
        
    except AttributeError as e:
        return jsonify({'message': 'Bad Request'}), 400
