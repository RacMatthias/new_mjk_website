from . import db


class Artwork(db.Model):
    id = db.Column("artwork_id", db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    size = db.Column(db.String(50))
    technique = db.Column(db.String(200))
    path_to_image = db.Column(db.String(200))

    def __init__(self, title, size, technique, path_to_image):
        self.title = title
        self.size = size
        self.technique = technique
        self.path_to_image = path_to_image

    def __repr__(self):
        return f"Title: {self.title}, Size: {self.size}"


class Admin(db.Model):
    id = db.Column("admin_id", db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"Username: {self.username}, Password: {self.password}"