from flask import Flask
from config import Config
from db_connection.connection import db
import models

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

    from events.routes import event_route
    app.register_blueprint(event_route, url_prefix='/events')

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'


if __name__ == '__main__':
    app.run()
