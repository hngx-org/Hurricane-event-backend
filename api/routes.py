from flask import Blueprint, jsonify, request
import json
from models.user import *

api = Blueprint('api', __name__)

@api.route('/user/profile', methods=['GET'])
def get_user_details():
    id = None

    if 'id' in request.args:
        # Get id from URL parameter
        id = request.args["id"]
    elif request.is_json:
        # Get id from JSON payload
        data = request.get_json()
        if 'id' in data:
            id = data['id']

    if id:
        # Get user's details
        user = User.query.get(id)
        if user:
            user_data = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'access_token': user.access_token,
                'refresh_token': user.refresh_token,
                'avatar': user.avatar
            }

            result = json.dumps(user_data, indent=4)
            return result, 201, {'Content-Type': 'application/json'}
        else:
            return jsonify(message='User not found'), 404
    else:
        return jsonify(message='Invalid request or missing id')