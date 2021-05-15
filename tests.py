import unittest, os

from app import app, db

from app.models import User, TestAttempt


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
        self.assertNotEqual(u1.username, 'User1')
        self.assertNotEqual(u1.username, 'User2')

    def test_test_scores(self):
        u1 = User(username = 'user1')
        u2 = User(username = 'user2')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
      
        # Need a test_attempt function!
        # self.assertEqual(len(u1.testAttempts), 0) #Need to make sure test scores start at 0 for all of them
        t1 = TestAttempt(student = u1)
        t1_1 = TestAttempt(student = u1)
        t2 = TestAttempt(student = u1)
        t3 = TestAttempt(student = u1)

        test1u2 = TestAttempt(student = u2)
        test2u2 = TestAttempt(student = u2)
        test3u2 = TestAttempt(student = u2)


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
        testsu1 = u1.testAttempts.all()

        # Check that valid inputs are added correctly
        self.assertEqual(testsu1[0].testId, 1)
        self.assertEqual(testsu1[0].score, 10)
        self.assertEqual(testsu1[1].score, 100)
        self.assertNotEqual(testsu1[1],55)
        self.assertTrue(t1.checkCorrectScore(10))
        self.assertFalse(t1.checkCorrectScore(0))   

        # Check that invalid inputs are not added
        test1u2.addTestScore(1,-1)
        test1u2.addTestScore(4,50)
        test1u2.addTestScore(-1,50)
        testsu2 = u2.testAttempts.all()
        for i in range(len(testsu2)):
            self.assertEqual(testsu2[i].testId, None)
            self.assertEqual(testsu2[i].score, None)
        

 
        db.session.commit()       
        

if __name__ =='__main__':
    unittest.main(verbosity = 2)
