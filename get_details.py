from flask import Flask, jsonify
from models.group import Group

app = Flask(__name__)
MAX_NO_OF_IMAGES = 2
def to_dict(obj):
    data = {}
    for field in obj.__table__.columns:
        value = getattr(obj, field.name)
        if isinstance(value, set):
            # Convert sets to lists 
            data[field.name] = list(value)
        else:
            data[field.name] = value
    return data
@app.route("/api/groups/<group_id>", methods=["GET"])

""""
@api_views.route("groups/<group_id>/all")
def group_details(group_id):
    # check if a group exists with this id
    group = models.storage.get("Group", group_id)
    if not group:
        return jsonify({"error": "Group doesn't exist!"}), 404
    group_events = group.events
    user_groups = group.users

    group_details = {
        "name": group.title,
        "events": [event.to_dict() for event in group_events],
        "users": [user.to_dict() for user in user_groups]
        }
    
    return jsonify({"details": group_details}), 200
"""


if __name__ == "__main__":
    app.run(debug=True)
