import models
from . import api_views
from models.event import Event
from models.comment import Comment
from flask import jsonify, request


@api_views.route("/events/<event_id>/comments", methods=["POST"])
def add_comment(event_id):
    """Adds a comment to an event"""
    data = request.get_json()
    body = data.get("body")
    user_id = data.get("user_id")
    image = data.get("image")

    event = models.storage.get("Event", event_id)

    if not event:
        return jsonify({"message": "Invalid Event ID"}), 404

    if body and user_id:
        comment = Comment(body, user_id, event_id)
        comment.save()

        if image:
            comment.update(image=image)
            comment.save()
        return jsonify({"message": "success"}), 201
    return jsonify({"message": "Incomplete comment details"}), 412


@api_views.route("/events/<event_id>/comments")
def get_comment(event_id):
    """Gets comments of an event"""
    event = models.storage.get("Event", event_id)
    if event:
        comments = event.comments
        comment_dict = [comment.to_dict() for comment in comments]

        return jsonify(comment_dict)
    return jsonify({"message": "Invalid Event ID"}), 404


@api_views.route("/comments/<comment_id>/images", methods=["POST"])
def add_comment_img(comment_id):
    """Adds an image to a comment"""
    image = request.get_json().get("image")

    comment = models.storage.get("Comment", comment_id)
    if comment:
        if image:
            comment.update(image=image)
            comment.save()

            return jsonify({"message": "success"}), 201
        return jsonify({"message": "Image url was not passed"}), 412
    return jsonify({"message": "Invalid Comment ID"}), 404


@api_views.route("/comments/<comment_id>/images")
def get_comment_img(comment_id):
    """Gets an image from comments"""
    comment = models.storage.get("Comment", comment_id)
    if comment:
        obj = {"image_url": comment.image,
               "comment_id": comment_id}
        return jsonify(obj)
    return jsonify({"message": "Invalid Comment ID"}), 404
