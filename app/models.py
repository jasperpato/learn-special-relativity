from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    testAttempts = db.relationship('TestAttempt', backref = 'student', lazy = 'dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class TestAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    testId = db.Column(db.Integer) # 1, 2 or 3
    score = db.Column(db.Integer)
    date = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Test {}; Score {}>'.format(self.testId, self.score)