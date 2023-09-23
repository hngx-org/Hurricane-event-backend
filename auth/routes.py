# Authentication routes here
from flask import Blueprint, jsonify, request
from models.user import User
import models


auth = Blueprint('auth', __name__)
auth.config = {}  # This helps avoid the "Blueprint does not have config" error


@auth.route('/users/login', methods=['POST'])
def login():
    data = request.get_json('payload')
    user_info = data.get('userinfo')
    email = user_info.get('email')

    user = models.storage.getUser(User, email)
    if not user:
        new_user = User(name=user_info.get('name'), email=email,
                        avatar=user_info.get('picture'))
        new_user.save()
        user = models.storage.getUser(User, email)
    return jsonify(user_id=user.id, name=user.name, email=user.email, avatar=user.avatar), 200
