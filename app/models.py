from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(64), index = True, unique = True)
    admin = db.Column(db.Boolean)
    
    password_hash = db.Column(db.String(128))

    testAttempts = db.relationship('TestAttempt', backref = 'student', lazy = 'dynamic')

    def __repr__(self):

        return '<User {}>'.format(self.username)
    
class TestAttempt(db.Model):

    attemptId = db.Column(db.Integer, primary_key = True)

    testId = db.Column(db.Integer) # 1, 2 or 3
    score = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Test {}; Score {}>'.format(self.testId, self.score)