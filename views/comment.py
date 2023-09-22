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


"""
    A POST Endpoint that adds a like to a comment
"""
@comment_likes_bp.route('/api/<int:comment_id>/<string:user_id>/likes', methods=['POST'])
@jwt_required
def add_like_to_comment(comment_id, user_id):
    comment = Comment.query.get(comment_id)

    # Check if the comment exists
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    # Check if the user has already liked the comment
    if user_id in comment.likes:
        return jsonify({"error": "User has already liked this comment"}), 400

    try:
        # Append the user_id to the comment's likes and save
        comment.likes.append(user_id)
        models.storage.save()

        return jsonify(
            {
                'success': True,
                'comment_id': comment.id,
                'likes': comment.likes
            }
        )
    except Exception as e:
        models.storage.session.rollback()
        return jsonify({"error": str(e)}), 500