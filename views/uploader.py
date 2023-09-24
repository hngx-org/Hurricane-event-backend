from os import getenv
from . import api_views
import cloudinary
import cloudinary.uploader
from flask import request, jsonify

cloudinary.config(cloud_name=getenv("CLOUD_NAME"), api_key=getenv("CLOUD_KEY"),
                  api_secret=getenv("CLOUD_SECRET"))


@api_views.route("/image-upload", methods=["POST"])
def upload_image():
    """Uploads an image"""
    if "image" not in request.files:
        return jsonify({"message": "No image in request"}), 400
    image = request.files["image"]
    if image.filename == "":
        return jsonify({"message": "No image selected"}), 400
    if image:
        result = cloudinary.uploader.upload(image)
        return jsonify({"message": "success", "url": result["secure_url"]})
    return jsonify({"message": "Unidentified error"}), 500
