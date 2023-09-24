from flask import Blueprint, request
import json
import requests
import jwt

api_views = Blueprint("api_views", __name__)


@api_views.before_request
def authenticate_request():
    rule = request.url_rule
    if rule and (rule.rule != "/api/test/auth") and (rule.rule != "/api/test/others"):
        return
    try:
        data = json.loads(request.data)
        email = data.get('email')
        google_token = data.get('access_token')
        if email and google_token:
            query = {"access_token": google_token}
            token_url = "https://www.googleapis.com/oauth2/v3/tokeninfo"
            response = requests.get(token_url, params=query)

            if response.status_code == 200:
                token_info = response.json()
                if token_info.get("email") == email:
                    return
    except json.JSONDecodeError:
        pass
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "No Authorization header"}), 401
    try:
        data = jwt.decode(token, current_app.secret_key, algorithms=['HS256'])
    except jwt.DecodeError:
        return jsonify({"message": "Invalid Authorization"}), 401


from views.comment import *
from views.event import *
from views.group import *
from views.user import *
