from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    testAttempts = db.relationship('TestAttempt')
    theme = db.Column(db.String(64))
    
    def __repr__(self): return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def best_attempt(self, test_num):
        attempts = TestAttempt.query.filter_by(test_number=test_num, user_id=self.id).all()
        max = 0
        for attempt in attempts:
            if attempt.score > max: max = attempt.score
        return max

    def first_attempt(self, test_number):
        first = TestAttempt.query.filter_by(test_number=test_number, user_id=self.id, attempt_number=1).first()
        return first.score if first else 0

    def selected_theme(self): return self.theme

    def set_theme(self, theme):
        if theme in ('Blue', 'Green','Purple','Red'): self.theme = theme

class TestAnswer(db.Model):
    __tablename__ = 'test_answer'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(100))
    correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey('test_question.id'))
    db.UniqueConstraint('number', 'question_id')

class TestQuestion(db.Model):
    __tablename__ = 'test_question'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(100))
    answer = db.Column(db.String(100))
    answers = db.relationship('TestAnswer')
    test_number = db.Column(db.Integer, db.ForeignKey('test.number'))
    db.UniqueConstraint('number', 'test_number')

    def get_correct(self):
        if self.answers == []: return self.answer
        for a in self.answers:
            if a.correct: return str(a.number)

class Test(db.Model):
    __tablename__ = 'test'
    number = db.Column(db.Integer, primary_key=True)
    questions = db.relationship('TestQuestion')

class TestAttempt(db.Model):
    __tablename__ = 'test_attempt'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    attempt_number = db.Column(db.Integer)
    test_number = db.Column(db.Integer, db.ForeignKey('test.number'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self): return '<Test {}; Score {}>'.format(self.test_number, self.score)
    
    def addTestScore(self, testNum, score):
        if testNum in (1,2,3) and score >= 0 and score <= 100:
            self.test_number = testNum
            self.score = score
            
    def checkCorrectScore(self,inputScore): return self.score == inputScore
