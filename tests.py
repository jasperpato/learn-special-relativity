import unittest
import main
from app import auth, db
from app.models import User, TestAttempt
from datetime import datetime, timedelta
# from selenium import webdriver #Not currently used but useful for further testing

class UsersTest(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def test_password_hashing(self):

        u = User(username = 'checkingUser')
        u.password_hash('passw0rd')
        
        self.assertFalse(u1.check_password_hash('password'))
        self.asserTrue(u1.check_password_hash('passw0rd'))

    def test_usernames(self):
        u1 = User(username = 'user1')
        u2 = User(username = 'user2')

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        with self.assertRaises(UserExists):
            u3 = User(username = 'user1')

    def test_test_scores(self):
        u1 = User(username = 'user1')
        u2 = User(username = 'user2')

        db.session.add(u1)
        db.session.add(u2)
        
        

if __name__ =='__main__':
    unittest.main(verbosity = 2)
