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
def group_details(group_id):
    # check if a group exists with this id
    group = Group.query.filter_by(id=group_id).first()
    if not group:
        return jsonify({"error": "Group doesn't exist!"}), 404

    group_details = {
        "name": group.title,
        "events": [to_dict(event) for event in group.events],
        "images": [to_dict(image) for image in group.images[:MAX_NO_OF_IMAGES]],
        "users": [to_dict(user) for user in group.users]}
    
    return jsonify({"details": group_details}), 200



if __name__ == "__main__":
    app.run(debug=True)
