from sqlalchemy.sql.functions import random
from models import db


class Questions(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer1 = db.Column(db.String, nullable=False)
    answer2 = db.Column(db.String, nullable=False)
    answer3 = db.Column(db.String, nullable=False)
    answer4 = db.Column(db.String, nullable=False)
    correct = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)

    @classmethod
    def select_question(cls, num: int, question_type: int):
        return cls.query.filter_by(type=question_type).order_by(random()).limit(num)
