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
        test2u2.addTestScore(4,50)
        test3u2.addTestScore(-1,50)
        db.session.commit() 
        testsu2 = u2.testAttempts.all()
        for i in range(len(testsu2)):
            self.assertEqual(testsu2[i].testId, None)
            self.assertEqual(testsu2[i].score, None)
         

    def test_best_attempt(self):
        uba = User(username = 'testBA')
        db.session.add(uba)
        test1attem1 = TestAttempt(student = uba)
        test1attem2 = TestAttempt(student = uba)
        test1attem3 = TestAttempt(student = uba)

        test2attem1 = TestAttempt(student = uba)
        test2attem2 = TestAttempt(student = uba)
        test2attem3 = TestAttempt(student = uba)

        test3attem1 = TestAttempt(student = uba)
        test3attem2 = TestAttempt(student = uba)
        test3attem3 = TestAttempt(student = uba)

        test1inv1   = TestAttempt(student = uba)
        test2inv1   = TestAttempt(student = uba)
        test3inv1   = TestAttempt(student = uba)
        testinv2    = TestAttempt(student = uba) 

        test1attem1.addTestScore(1,10)
        test1attem2.addTestScore(1,55)
        test1attem3.addTestScore(1,19)

        test2attem1.addTestScore(2,22)
        test2attem2.addTestScore(2,10)
        test2attem3.addTestScore(2,11)

        test3attem1.addTestScore(3,69)
        test3attem2.addTestScore(3,6)
        test3attem3.addTestScore(3,71)



        #Invalid inputs, 101 > 100
        test1inv1.addTestScore(1,101) 
        test2inv1.addTestScore(2,101) 
        test3inv1.addTestScore(3,101) 

        testinv2.addTestScore(4,100) 
        db.session.commit()
        self.assertNotEqual(uba.best_attempt(1), 101)
        self.assertNotEqual(uba.best_attempt(2), 101)
        self.assertNotEqual(uba.best_attempt(3), 101)

        self.assertNotEqual(uba.best_attempt(1), 19)
        self.assertNotEqual(uba.best_attempt(2), 11)
        self.assertNotEqual(uba.best_attempt(3), 6)

        self.assertEqual(uba.best_attempt(1), 55)
        self.assertEqual(uba.best_attempt(2), 22)
        self.assertEqual(uba.best_attempt(3), 71)
    
    def test_select_theme(self):
        setThemeUser = User(username = 'themeTest')
        setThemeUser.set_password('coolThemesdotcom')
        db.session.add(setThemeUser)
        db.session.commit()

        setThemeUser.set_theme("Blue")
        self.assertEqual(setThemeUser.theme,"Blue")
        self.assertNotEqual(setThemeUser.theme,"Red")
        self.assertNotEqual(setThemeUser.theme,"Green")
        self.assertNotEqual(setThemeUser.theme,"Purple")

        setThemeUser.set_theme("Green")
        self.assertEqual(setThemeUser.theme,"Green")
        self.assertNotEqual(setThemeUser.theme,"Blue")
        self.assertNotEqual(setThemeUser.theme,"Purple")
        self.assertNotEqual(setThemeUser.theme,"Red")

        setThemeUser.set_theme("Red")
        self.assertEqual(setThemeUser.theme,"Red")
        self.assertNotEqual(setThemeUser.theme,"Purple")
        self.assertNotEqual(setThemeUser.theme,"Green")
        self.assertNotEqual(setThemeUser.theme,"Blue")


        setThemeUser.set_theme("Purple")
        self.assertEqual(setThemeUser.theme,"Purple")
        self.assertNotEqual(setThemeUser.theme,"Green")
        self.assertNotEqual(setThemeUser.theme,"Blue")
        self.assertNotEqual(setThemeUser.theme,"Red")


        



    def test_selected_theme(self):
        themeUser = User(username = 'themeTest')
        themeUser.set_password('coolThemesdotcom')
        db.session.add(themeUser)
        db.session.commit()
        themeUser.set_theme("Blue")
        self.assertEqual(themeUser.selected_theme(),"Blue")
        self.assertNotEqual(themeUser.selected_theme(),"Red")
        self.assertNotEqual(themeUser.selected_theme(),"Green")
        self.assertNotEqual(themeUser.selected_theme(),"Purple")

        themeUser.set_theme("Red")
        self.assertEqual(themeUser.selected_theme(),"Red")
        self.assertNotEqual(themeUser.selected_theme(),"Blue")
        self.assertNotEqual(themeUser.selected_theme(),"Green")
        self.assertNotEqual(themeUser.selected_theme(),"Purple")

        themeUser.set_theme("Green")
        self.assertEqual(themeUser.selected_theme(),"Green")
        self.assertNotEqual(themeUser.selected_theme(),"Blue")
        self.assertNotEqual(themeUser.selected_theme(),"Red")
        self.assertNotEqual(themeUser.selected_theme(),"Purple")

        themeUser.set_theme("Purple")
        self.assertEqual(themeUser.selected_theme(),"Purple")
        self.assertNotEqual(themeUser.selected_theme(),"Blue")
        self.assertNotEqual(themeUser.selected_theme(),"Red")
        self.assertNotEqual(themeUser.selected_theme(),"Green")
    
    def test_select_theme_invalid_input(self):
        invalidInput = User(username = 'invalidIputTest')
        invalidInput.set_password('theSmoker??')
        db.session.add(invalidInput)
        db.session.commit()

        invalidInput.set_theme("Blurple")
        self.assertNotEqual(invalidInput.selected_theme(),"Blurple")
        self.assertEqual(invalidInput.selected_theme(),None)

        invalidInput.set_theme("")
        self.assertNotEqual(invalidInput.selected_theme(),"")
        self.assertEqual(invalidInput.selected_theme(),None)   
        

if __name__ =='__main__':
    unittest.main(verbosity = 2)
