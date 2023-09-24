from flask import Flask, jsonify
import models
from views import api_views

app = Flask(__name__)
app.config["SECRET_KEY"] = "_HuRrIcAnE_eVeNt_ApP_"
app.register_blueprint(api_views, url_prefix="/api")


@app.errorhandler(404)
def not_found(exception):
    """URL Not found"""
    return jsonify({"message": "Url Not found"}), 404


@app.errorhandler(415)
def not_json(exception):
    """Data is not JSON"""
    return jsonify({"message": "Media Type is not JSON"}), 415


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Internal server error contact admin'}), 500


@app.teardown_appcontext
def close_database(exception):
    """Loads data into session from database"""
    models.storage.close()


@app.route('/')
def hello_world():  # put application's code here
    return jsonify({"message": "Hello World!"})


# # Register the blueprints for each package here
# app.register_blueprint(group_bp, url_prefix='/groups')
# app.register_blueprint(event, url_prefix='/events')
# app.register_blueprint(auth, url_prefix='/api')
# app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run()
