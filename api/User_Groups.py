from flask import Flask, jsonify, Blueprint
from models import Group, User  # Import from models
from db_connection.connection import db

app = Flask(__name__)

api_bp = Blueprint('api', __name__)

@api_bp.route('/<int:userid>/groups', methods=['GET'])
def get_user_groups(userid):
    user = User.query.get(userid)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    groups = Group.query.filter_by(user_id=userid).all()
    group_list = [{'id': group.id, 'name': group.name} for group in groups]

    return jsonify({'user_id': userid, 'groups': group_list})



# Register the API blueprint with a URL prefix
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
