from flask import Flask
# from config import Config
# from db_connection.connection import db
import models

app = Flask(__name__)

# app.config.from_object(Config)
# db.init_app(app)


@app.teardown_appcontext
def close_database():
    """Loads data into session from database"""
    models.storage.close()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
