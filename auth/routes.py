# Authentication routes here
from flask import Blueprint, jsonify, request
import os
from models.user import User
from authlib.integrations.flask_client import OAuth
import models
from sqlalchemy.orm.exc import NoResultFound


auth = Blueprint('auth', __name__)
auth.config = {}  # This helps avoid the "Blueprint does not have config" error

@auth.route('users/login', methods=['POST'])
def login():
    data = request.json.get('payload')
    user_info = data.get('userinfo')
    email = user_info.get('email')

    try:
        user = models.storage.getUser(User, email)
    except NoResultFound:
        new_user = User(name=user_info.get('name'), email=email, avatar=user_info.get('picture'))
        new_user.save()
        user = models.storage.getUser(User, email)
        return jsonify(user_id=user.id, name=user.name, email=user.email, avatar=user.avatar), 200
    else:
        return jsonify(user_id=user.id, name=user.name, email=user.email, avatar=user.avatar), 200
