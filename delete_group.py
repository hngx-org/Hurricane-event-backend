from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.group import Group
from models.user_group import user_groups


app = Flask(__name__)
'''connecting to the database at which in my case I'm using  SQLAlchemy connected to sqlite
and it's a local file so we don't need username and password for this one'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # replace with your database URI for now I'm sing test.db
db = SQLAlchemy(app)

'''creating the database model 
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groups = db.relationship('Group', backref='user', lazy='dynamic')

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
''' defining the end point with method delete
'''
@app.route('/api/<int:userId>/groups/<int:groupId>', methods=['DELETE'])
def delete_group(userId, groupId):
     #    print("User", userId,"Group:", "groupId")
    user = User.query.get(userId)
    group = Group.query.get(groupId)

   
     # Check if the user or group exists
    if not user:
        return {"error": "User not found"}, 404
    
    
    # Check if the user is in the group
    group = Group.query.filter_by(id=groupId, user_id=userId).first()
    if not group:
        return {"error": "Group not found"}, 404
    db.session.delete(group)
    db.session.commit()
    return {"message": "Group was successfully deleted"}, 200
