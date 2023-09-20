from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from models.event import db, events
from datetime import datetime
from config import Config
from db_connection.connection import db
import models

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'database_url'
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)


with app.app_context():
    db.create_all()

    @app.route('/api/events', methods=['POST'])
    @jwt_required()
    def create_event():  # put application's code here
        try:
            data = request.get_json()

            # Extract event data from the JSON request

            title = data['title']
            description = data['description']
            location = data['location']
            group_id = data.get('group_id')
            start_date = data['start_date']
            start_time = data['start_time']
            end_date = data['end_date']
            end_time = data['end_time']
            thumbnail_url = data['thumbnail_img_url']
            user_id = get_jwt_identity()

            # Save the event to the database
            new_event = events(
                title=title,
                description=description,
                location=location,
                start_date=start_date,
                start_time=start_time,
                end_date=end_date,
                end_time=end_time,
                thumbnail=thumbnail_url,
                creator_id=user_id
            )

            db.session.add(new_event)
            db.session.commit()

            return jsonify(message="Event created successfully"), 201

        except Exception as e:
            return jsonify(error=str(e)), 400


if __name__ == '__main__':
    app.run(debug=True)
