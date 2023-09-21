from flask import Flask, jsonify, Blueprint
from models import User, Event  # Import necessary models
from db_connection.connection import db

app = Flask(__name__)

# Define an API blueprint
api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/users/<int:userid>/events', methods=['GET'])
def get_user_events(userid):
    # Retrieve the user from the database
    user = User.query.get(userid)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Retrieve events associated with the specified user
    signed_up_events = user.events 

    event_list = [
        {
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'location': event.location,
            'start_date': str(event.start_date),  # Convert date objects to strings
            'end_date': str(event.end_date),
            'start_time': str(event.start_time),  # Convert time objects to strings
            'end_time': str(event.end_time),
            'thumbnail_url': event.thumbnail_url,
            'creator_id': event.creator_id 
        }
        for event in signed_up_events
    ]

    return jsonify({'user_id': userid, 'events': event_list})

# Register the API blueprint with a URL prefix
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run()
