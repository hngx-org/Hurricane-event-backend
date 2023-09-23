from flask import Blueprint, jsonify, request, current_app, redirect, url_for
from models.user import User
import models
import jwt
from datetime import datetime, timedelta
from functools import wraps
import requests

auth = Blueprint('auth', __name__)
auth.config = {}  # This helps avoid the "Blueprint does not have config" error

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):

        data = request.get_json()
        email = data.get('email')
        google_token = data.get('access_token')
        if email and google_token:
            token_url = f"https://www.googleapis.com/oauth2/v3/tokeninfo?access_token={google_token}"
            response = requests.get(token_url)
            if response.status_code == 200:
                token_info = response.json()
                if token_info.get(email) == email:
                    return func(*args, **kwargs)
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": 'No Authorization token attached'}), 400
        try:
            data = jwt.decode(token, current_app.secret_key, algorithms=['HS256'])
        except jwt.DecodeError:
            return jsonify(response='Invalid Token'), 403

        return func(*args, **kwargs)



@auth.route("/auth", methods=["POST"])
@token_required
def authenticate_user():
    """Authenticates a user
    Returns: user_id
    """
    data = request.get_json()
    email = data.get("email")
    name = data.get("name")
    avatar = data.get("avatar")

    if email:
        users = models.storage.search("User", email=email)
        if users:
            user = users[0]
        else:
            if name:
                user = User(name, email, avatar)
                user.save()
            else:
                return jsonify({"message": "No name found"}), 412
        token = jwt.encode({
            'user': user.id,
            'email': user.email,
            # 'exp': datetime.utcnow() + timedelta(hours=1)
        },
            current_app.secret_key, algorithm='HS256')
        return jsonify({"user_id": user.id, "Authorization_token": token}), 201
    return jsonify({"message": "No email found"}), 412

