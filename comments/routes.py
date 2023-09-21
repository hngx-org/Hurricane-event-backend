from flask import Blueprint, abort, jsonify
import models
from models.comment import Comment
from models.image import Image

comment_bp = Blueprint('comments', __name__)

""""
    A GET endpoint that returns all images related to a comment.
"""

@comment_bp.route('/comments/<int:comment_id>/images', methods=['GET'])
def get_comment_images(comment_id):
    try:
        # This is basically meant to check if the comment exists in the database
        # gets the comment with the given comment_id returns the comment in success or None
        comment = models.storage.get(Comment, comment_id)
        
        if comment is None:
            pass
        
        # fetch from the database, all the images related to the comment
        images = models.storage.getImages(Image, comment)

        # return all the images related to the comment
        return jsonify(images=[image.to_dict() for image in images])
    except Exception as e:
        Comment.storage.session.rollback()
        return jsonify({"error": e}), 404
    
