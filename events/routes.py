# Routes for handling event related functionality (event creation, updating and deleting)

from flask import Flask, request, jsonify
from db_connection.connection import db
from models import Event, InterestedEvent, Comment, GroupEvent

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
        db.session.add(comment)
        db.session.commit()
        return jsonify({'message': 'Comment added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
