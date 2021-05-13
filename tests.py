import unittest, os

from app import app, db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import User, TestAttempt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func

# from selenium import webdriver #Not currently used but useful for further testing tim
# Need statistics testing No dividing by 0
# Need to make sure all complex tests don't just have assertTrue make more interesting


class UsersTest(unittest.TestCase):

    def setUp(self):

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all() 

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def test_password_hashing(self):

        u = User(username = 'checkingUser',password_hash=generate_password_hash("passw0rd", method='sha256'))
        
        self.assertFalse(check_password_hash(u.password_hash,'password'))
        self.assertTrue(check_password_hash(u.password_hash,'passw0rd'))
        self.assertNotEqual(u.password_hash, 'passw0rd')

    def test_usernames(self):
        u1 = User(username = 'user1')
        u2 = User(username = 'user2')

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.username, 'user1')
        self.assertEqual(u2.username, 'user2')

    def test_test_scores(self):
        u1 = User(username = 'user1',password_hash=generate_password_hash("password1", method='sha256'),)
        u2 = User(username = 'user2',password_hash=generate_password_hash("password2", method='sha256'))
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        print("This is attempt",u1.testAttempts)
        # Need a test_attempt function!
        # self.assertEqual(len(u1.testAttempts), 0) #Need to make sure test scores start at 0 for all of them
        u1.testAttempts(id = u1, testId = 1, score = 100)
        # test1u1 = TestAttempt(id = u1, testId = 1, score = 100)
        # test2u1 = TestAttempt(id = u1, testId = 2, score = 100, date = datetime.date())
        # test3u1 = TestAttempt(id = u1, testId = 3, score = 100, date = datetime.date())

        # test1u2 = TestAttempt(id = u2, testId = 1, score = 100, date = datetime.date())
        # test2u2 = TestAttempt(id = u2, testId = 2, score = 100, date = datetime.date())
        # test3u2 = TestAttempt(id = u2, testId = 3, score = 100, date = datetime.date())
        # u1.testAttempts(test1u1)
        # u1.testAttempts(test2u1)
        # u1.testAttempts(test3u1)
        # u2.testAttempts(test1u1)
        # u2.testAttempts(test2u1)
        # u2.testAttempts(test3u1)
        db.session.commit()       
        

if __name__ =='__main__':
    unittest.main(verbosity = 2)
