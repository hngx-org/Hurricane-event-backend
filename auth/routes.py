# Authentication routes here
from flask import Blueprint, jsonify, request, current_app, redirect, url_for
from models.user import User
import models
import jwt
from datetime import datetime, timedelta
from functools import wraps

auth = Blueprint('auth', __name__)
auth.config = {}  # This helps avoid the "Blueprint does not have config" error

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": 'No Authorization token attached', "redirect_url": url_for('signup')}), 400
        try:
            data = jwt.decode(token, current_app.secret_key, algorithms=['HS256'])
        except jwt.DecodeError:
            return jsonify(response='Invalid Token'), 403
        return func(*args, **kwargs)

@auth.route("/auth/login", methods=["POST"])
@token_required
def authenticate_user():
    """Authenticates a user
    Returns: user_id
    """
    data = request.get_json()
    email = data.get("email")
    name = data.get("name")
    avatar = data.get("avatar")
    token = request.headers.get('Authorization')
    data = jwt.decode(token, current_app.secret_key, algorithms=['HS256'])
    token_email = data.get('email')

    if email == token_email:
        users = models.storage.search("User", email=email)
        if users:
            user = users[0]

            token = jwt.encode({
                'user': user.id,
                'email': user.user,
                # 'exp': datetime.utcnow() + timedelta(hours=1)
            },
            current_app.secret_key, algorithm='HS256')
            return jsonify({"user_id": user.id, "Authorization_token": token})
    return jsonify({"message": "Token data does not match"}), 400

@auth.route("/auth/signup", methods=["POST"])
def signup():
    """Sign up new users"""
    data = request.get_json()
    email = data.get("email")
    name = data.get("name")
    avatar = data.get("avatar")
    if name:
        new_user = User(name, email, avatar)
        new_user.save()
        user = models.storage.search("User", email=email)
        token = jwt.encode({
            'user': user.id,
            'email': user.user,
            # 'exp': datetime.utcnow() + timedelta(hours=1)
        },
            current_app.secret_key, algorithm='HS256')
        return jsonify({"user_id": user.id, "Authorization_token": token}), 201