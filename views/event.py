import models
from . import api_views
from models.event import Event
from models.interested_event import interested_events
from flask import jsonify, request


@api_views.route("/events", methods=["POST"])
def create_event():
    """Creates an event"""
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    location = data.get("location")
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    creator_id = data.get("creator_id")
    thumbnail = data.get("thumbnail")

    event_info = {"title": title, "location": location,
                  "start_date": start_date, "end_date": end_date,
                  "start_time": start_time, "end_time": end_time,
                  "creator_id": creator_id
                  }
    for key, value in event_info.copy().items():
        if not value:
            event_info.pop(key)
    if len(event_info) < 7:
        return jsonify({"message": "Incomplete event details"}), 412
    event_info["description"] = description
    event_info["thumbnail"] = thumbnail
    event = Event(**event_info)
    event.save()
    return jsonify({"message": "success"}), 201


@api_views.route("/events")
def get_events():
    """Gets all the list of events
    Recommendation: not all details
    """
    events = models.storage.all("Event")
    events_dict = [{"id": event.id,
                    "title": event.title,
                    "description": event.description,
                    "start_date": event.start_date.isoformat(),
                    "creator_id": event.creator_id
                    } for event in events]
    return jsonify(events_dict), 200


@api_views.route("/events/<event_id>")
def get_event(event_id):
    """Get an event resource"""
    try:
        event = models.storage.get("Event", event_id)
        return jsonify(event.to_dict())
    except:
        return jsonify({"message": "Event not found"}), 404


@api_views.route("/events/<event_id>", methods=["PUT"])
def update_event(event_id):
    """Updates an event resource"""
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    location = data.get("location")
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    creator_id = data.get("creator_id")
    thumbnail = data.get("thumbnail")

    update_info = {"title": title, "description": description,
                   "location": location, "start_date": start_date,
                   "end_date": end_date, "start_time": start_time,
                   "end_time": end_time, "creator_id": creator_id,
                   "thumbnail": thumbnail
                   }
    for key, value in update_info.copy().items():
        if not value:
            update_info.pop(key)
    if update_info:
        try:
            event = models.storage.get("Event", event_id)
            event.update(**update_info)
            event.save()
            return jsonify({"message": "success"}), 202
        except:
            return jsonify({"message": "User ID does not exist"}), 404
    return jsonify({"message": "unchanged"})


@api_views.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    """Deletes an event resource"""
    event = models.storage.get("Event", event_id)
    if event:
        models.storage.delete("Event", event.id)
        models.storage.save()
        return jsonify({"message": "success"})
    return jsonify({"message": "Resource UID not found"}), 404


@api_views.route("/events/<user_id>/events")
def interested_events(user_id):
    '''Gets all events a user is interested in'''
    user = models.storage.get("User", user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    interested_events = user.events

    events = [event.to_dict() for event in interested_events]
    return jsonify({'user': user.name, 'events': events})
