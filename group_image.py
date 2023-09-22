from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

# group_image association table
group_image = db.Table(
    "group_image",
    db.Column("group_id", db.String(60), db.ForeignKey("group.id")),
    db.Column("image_id", db.String(225), db.ForeignKey("image.id"))
)