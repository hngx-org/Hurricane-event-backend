# Authentication routes here
from flask import Blueprint, redirect, url_for, jsonify, request, session, current_app
import os
from models.user import User
from authlib.integrations.flask_client import OAuth
from models import storage
from sqlalchemy.orm.exc import NoResultFound
import jwt
from functools import wraps
import os


CLIENT_ID = os.environ.get('client_id') # ID gotten from Google
CLIENT_SECRET = os.environ.get('client_secret') # Secret from Google
OAUTH2_META_URL = 'https://accounts.google.com/.well-known/openid-configuration'

auth = Blueprint('auth', __name__)

oauth = OAuth(auth)
oauth.register(name='google',
               client_id=CLIENT_ID,
               client_secret=CLIENT_SECRET,
               client_kwargs={'scope': 'openid email profile'},
               server_metadata_url=OAUTH2_META_URL,

               )

def token_required(func):
    """For protected route"""
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('access_token')
        if not args:
            return jsonify(Response='access_token  is missing'), 401
        try:
            data = jwt.decode(token, current_app.secret_key)
        except jwt.DecodeError:
            return jsonify(response='Invalid access_token '), 403
        return func(*args, **kwargs)


@auth.route('/users/login', methods=['GET'])
def signin():
    return oauth.google.authorize_redirect(redirect_uri=url_for('callback', _external=True))

@auth.route('/users/login/callback', methods=['GET'])
def callback():
    """
    retrieves user data from google auth
    """
    try:
        token = oauth.google.authorize_access_token()
    except Exception as e:
        return jsonify(alert='Not authorized'), 401
    data = dict(token)
    user_info = data.get('userinfo')
    email = user_info.get('email')
    return jsonify(url=url_for('login'), method='POST', email=email), 200


@auth.route('/users/login', methods=['POST'])
def login():
    """
    checks if the email already exist: if it does returns the User data with jwt token

    if it does not exist create, creates a user and session id
    """

    email = request.json.get('email')
    try:
        user = storage.session.execute(storage.select(User).filter_by(email=email)).scalar_one()
    except NoResultFound:
        return redirect(url_for('signup')), 307
    else:
        session['logged_in'] = True

        token = jwt.encode({
            'user': email,
        },
            current_app.secret_key)

        user.access_token = token
        storage.session.commit()

        return jsonify(access_token=user.access_token, name=user.name, email=user.email, response='Logged in successfully'), 200

