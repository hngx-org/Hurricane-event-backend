from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
