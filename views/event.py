import models
from . import api_views
from models.event import Event


@api_views.route("/events", methods=["POST"])
def create_event():
    """Creates an event"""
    pass


@api_views.route("/events")
def get_events():
    """Gets all the list of events
    Recommendation: not all details
    """
    pass


@api_views.route("/events/<event_id>")
def get_event(event_id):
    """Get an event resource"""
    pass


@api_views.route("/events/<event_id>", methods=["PUT"])
def update_event(event_id):
    """Updates an event resource"""
    pass


@api_views.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    """Deletes an event resource"""
    pass
