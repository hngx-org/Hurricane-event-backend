from flask import Flask, jsonify
from group.routes import group_bp
from events.routes import event_bp
from auth.routes import auth
from api.routes import api
import models
from views import api_views

app = Flask(__name__)
app.register_blueprint(api_views, url_prefix="/api")


@app.teardown_appcontext
def close_database(exception):
    """Loads data into session from database"""
    models.storage.close()

# status check
@app.route('/')
def hello_world():  # put application's code here
    return jsonify({"message": "Hello World!"})

# # Register the blueprints for each package here
# app.register_blueprint(group_bp, url_prefix='/groups')
# app.register_blueprint(event, url_prefix='/events')
# app.register_blueprint(auth, url_prefix='/auth')
# app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)