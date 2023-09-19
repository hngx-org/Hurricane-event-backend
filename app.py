from flask import Flask
from api.routes import api
from api.routes.auth import auth
from api.routes.user import user

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

