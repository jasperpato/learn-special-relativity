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

        u = User(username = 'checkingUser')
        u.set_password("passw0rd")
        self.assertFalse(u.check_password('password'))
        self.assertTrue(u.check_password('passw0rd'))
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
      
        # Need a test_attempt function!
        # self.assertEqual(len(u1.testAttempts), 0) #Need to make sure test scores start at 0 for all of them
        t1 = TestAttempt(testId = 1, student = u1)
        t1_1 = TestAttempt(testId = 1, student = u1)
        t2 = TestAttempt(testId = 2, student = u1)
        t3 = TestAttempt(testId = 3, student = u1)

        test1u2 = TestAttempt(student = u2)
        test2u2 = TestAttempt(testId = 2, score = 100,student = u2)
        test3u2 = TestAttempt(testId = 3, score = 100,student = u2)


        db.session.add(t1)
        db.session.add(t1_1)
        db.session.add(t2)
        db.session.add(t3)
        db.session.add(test1u2)
        db.session.add(test2u2)
        db.session.add(test3u2)
        db.session.commit()
        t1.addTestScore(1,10)
        t2.addTestScore(2, 55)
        t1_1.addTestScore(1,100)
        test = u1.testAttempts.all()
        for i in test:
            print(i)

        self.assertEqual(test[0].testId, 1)
        self.assertEqual(test[0].score, 10)
        self.assertEqual(test[1].score, 100)
        self.assertNotEqual(test[1],55)
        self.assertTrue(t1.checkCorrectScore(10))
        self.assertFalse(t1.checkCorrectScore(0))       
 
        db.session.commit()       
        

if __name__ =='__main__':
    unittest.main(verbosity = 2)
