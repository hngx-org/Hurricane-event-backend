from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    profile_pic = db.Column(db.String(255))

    def __init__(self, email, name, password, profile_pic=None):
        self.email = email
        self.name = name
        self.password = password
        self.profile_pic = profile_pic
