from app.models import db
from app.models import session_commit


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return "User(username={})".format(self.username)

    @classmethod
    def check_password(cls, username: str):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def change_password(cls, username: str, password: str):
        user = cls.query.filter_by(username=username).first()
        user.password = password
        return session_commit()

    def new_user(self):
        db.session.add(self)
        return session_commit()
