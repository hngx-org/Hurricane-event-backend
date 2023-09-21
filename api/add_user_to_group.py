from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.group import Group

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'our_db_uri' # Do we have a db uri yet? It goes here.
db = SQLAlchemy(app)



@app.route('/api/groups/<int:groupId>/members/<int:userId>', methods=['POST'])
def add_user_to_group(groupId, userId):

    # now, queries to get both the userId and groupId :)
    user = User.query.get(userId)
    group = Group.query.get(groupId)

    if not group:
        return jsonify({'error': 'Group not found'}), 404

    if not user:
        return jsonify({'error': 'User not found'}), 404

    group.members.append(user)
    db.session.commit()    

    return jsonify({'message': 'User added to the group successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)