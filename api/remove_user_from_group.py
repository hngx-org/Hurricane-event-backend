from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.group import Group

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'our_db_uri' # Do we have a db uri yet? It goes here.
db = SQLAlchemy(app)

@app.route('/api/groups/<int:groupId>/members/<int:userId>', methods=['DELETE'])
def remove_user_from_group(groupId, userId):
    # now, queries to get both the userId and groupId :)
    group = Group.query.get(groupId)
    user = User.query.get(userId)

    if not group: #if group doesn't exist do this :)
        return jsonify({'error': 'Group not found'}), 404 
    
    if not user: #if user doesn't exist do this :)
        return jsonify({'error': 'User not found'}), 404
    
    group.members.remove(user)
    db.session.commit()
    
    return jsonify({'message': 'User removed from the group successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)