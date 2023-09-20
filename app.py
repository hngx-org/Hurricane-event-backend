from flask import Flask
from config import Config
from db_connection.connection import db
import models
from api.routes import api
import models

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'


if __name__ == '__main__':
    app.run()
