from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    testAttempts = db.relationship('TestAttempt', backref = "student", lazy = "dynamic")
    theme = db.Column(db.String(64))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def best_attempt(self, test_num):
        attempts = TestAttempt.query.filter_by(testId = test_num, user_id = self.id).all()
        max = 0
        for attempt in attempts:
            if attempt.score > max:
                max = attempt.score
        return max

    def selected_theme(self):
        return self.theme

    def set_theme(self, theme):
        if theme in ("Blue", "Green","Purple","Red"):
            self.theme = theme

class TestAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    testId = db.Column(db.Integer) # 1, 2 or 3
    score = db.Column(db.Integer)
    date = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Test {}; Score {}>'.format(self.testId, self.score)
    
    def addTestScore(self, testNum, score):
        if testNum in (1,2,3) and score >= 0 and score <= 100:
            self.testId = testNum
            self.score = score
            
    def checkCorrectScore(self,inputScore):
        return(self.score == inputScore)
