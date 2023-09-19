from flask import Flask
from api.routes import api
from config import Config
from db_connection.connection import db
from database import models

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

