from flask import Flask
from config import Config
from db_connection.connection import db
from database import models

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
