import models# storage will be used for all db session based queries
from flask import Flask, jsonify, request, session
from models.user import User
from models.comment import Comment
from models.event import Event
from models.interested_event import InterestedEvent


# Routes for handling event related functionality (event creation, updating and deleting)

app = Flask(__name__)
app.config.from_object(Config)

# Route that adds a comment to an event
@app.route('/api/events/<int:event_id>/comments', methods=['POST'])
def add_comment(event_id):
    event = GroupEvent.query.get(event_id)
    if not event:
        return jsonify({'message': 'Event does not exist'}), 404

    body = request.json.get('body')
    if not body:
        return jsonify({'message': 'Comment is required'}), 400
    else:
        comment = Comment(body=body)
        event.comments.append(comment)
        models.storage.session.add(comment)
        models.storage.session.commit()
        return jsonify({'message': 'Comment added successfully'}), 201
