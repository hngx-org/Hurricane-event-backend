from auth import auth
from flask import Blueprint, request, jsonify
from database.models import User
from db_connection.connection import Session

api = Blueprint('api', __name__)

# Route to get all users
@api.route('/users', methods=['GET'])
def get_all_users():
    session = Session()
    users = session.query(User).all()
    session.close()

    user_list = [{'id': user.id, 'name': user.name, 'email': user.email, 'avatar': user.avatar} for user in users]
    return jsonify(user_list)

# Route to get a user based on email
@api.route('/users/<email>', methods=['GET'])
def get_user_by_email(email):
    session = Session()
    user = session.query(User).filter_by(email=email).first()
    session.close()

    if user:
        user_info = {'id': user.id, 'name': user.name, 'email': user.email, 'avatar': user.avatar}
        return jsonify(user_info)
    else:
        return jsonify({'error': 'User not found'}), 404
