from models import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return "User(username={})".format(self.username)

    def get_all(self):
        return self.query.all()
