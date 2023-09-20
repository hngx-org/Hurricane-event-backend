from flask import Flask
from config import Config
from db_connection.connection import db
import models

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'
    
    @app.route('/api/events/<string:group_id>/<string:event_id>', methods=['DELETE'])
    def delete_group_event(group_id,event_id):
    event = models.group_event.GroupEvent.query.filterby(event_id = event_id, group_id = group_id).first()
    
    if event:
        db.session.delete(event)
        db.session.commit()
        
        return jsonify({
            "message": "Event {event_id} deleted succesfully"
        }), 200
    
    else:
        return jsonify({
            "error": "Event not found"
        }), 404


if __name__ == '__main__':
    app.run()
