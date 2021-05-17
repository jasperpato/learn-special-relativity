import unittest, os, time
from app import app, db 
from app.models import User, TestAttempt
from selenium import webdriver
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

class SystemTest(unittest.TestCase):

    def setUp(self):
        path_to_chrome = basedir + "\chromedriver"
        self.driver = webdriver.Chrome(executable_path=path_to_chrome) 
        self.driver.get('http://127.0.0.1:5000/')
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.driver.close()
        
    
    def test_create_user_test(self):
        self.driver.get('http://127.0.0.1:5000/sign-up')
        self.driver.implicitly_wait(5)
        eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-')
        print('event id is', eventid)
        time.sleep(1)
        user_signup_sheet = self.driver.find_element_by_id("username")
        user_signup_sheet.send_keys(eventid)
        # time.sleep(10)
        self.driver.implicitly_wait(5)

        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('TimIsKing')
        user_password_confirm = self.driver.find_element_by_id("passwordConfirm")
        user_password_confirm.send_keys('TimIsKing')
        submit_button = self.driver.find_element_by_name("")
        submit_button.click()
        self.driver.implicitly_wait(5)

        #Created account successfully
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:5000/')
        self.assertNotEqual(self.driver.current_url,'http://127.0.0.1:5000/login')

        #Fails to make account since same username        
        self.driver.get('http://127.0.0.1:5000/sign-up')
        user_signup_sheet = self.driver.find_element_by_id("username")
        user_signup_sheet.send_keys(eventid)
        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('TimIsKing')
        user_password_confirm = self.driver.find_element_by_id("passwordConfirm")
        user_password_confirm.send_keys('TimIsKing')
        submit_button = self.driver.find_element_by_name("")
        submit_button.click()

        #Failed to make account
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:5000/sign-up')
        self.assertNotEqual(self.driver.current_url,'http://127.0.0.1:5000/')
        
        


    def test_take_tests(self):

        self.driver.get('http://127.0.0.1:5000/sign-up')
        self.driver.implicitly_wait(5)
        eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-')
        print('event id is', eventid)
        user_signup_sheet = self.driver.find_element_by_id("username")
        user_signup_sheet.send_keys(eventid)
        self.driver.implicitly_wait(5)

        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('coolUser')
        user_password_confirm = self.driver.find_element_by_id("passwordConfirm")
        user_password_confirm.send_keys('coolUser')
        submit_button = self.driver.find_element_by_name("")

        submit_button.click()

        self.driver.get('http://127.0.0.1:5000/learn/test-1')
        ans1_to_q1 = self.driver.find_element_by_id("1A")
        ans1_to_q2 = self.driver.find_element_by_id("2A")
        ans1_to_q3 = self.driver.find_element_by_id("3A")
        ans1_to_q4 = self.driver.find_element_by_id("4A")
        ans1_to_q5 = self.driver.find_element_by_id("5")
        submit_t1 = self.driver.find_element_by_id("submit")

        ans1_to_q1.click()
        ans1_to_q2.click()
        ans1_to_q3.click()
        ans1_to_q4.click()
        ans1_to_q5.send_keys("5")
        submit_t1.click()
        self.driver.implicitly_wait(5)

        self.driver.get('http://127.0.0.1:5000/learn/test-2')
        ans2_to_q1 = self.driver.find_element_by_id("1A")
        ans2_to_q2 = self.driver.find_element_by_id("2A")
        ans2_to_q3 = self.driver.find_element_by_id("3A")
        ans2_to_q4 = self.driver.find_element_by_id("4A")
        ans2_to_q5 = self.driver.find_element_by_id("5A")
        submit_t2 = self.driver.find_element_by_id("submit")

        ans2_to_q1.click()
        ans2_to_q2.click()
        ans2_to_q3.click()
        ans2_to_q4.click()
        ans2_to_q5.click()
        submit_t2.click()
        self.driver.implicitly_wait(5)


        self.driver.get('http://127.0.0.1:5000/learn/test-3')
        ans3_to_q1 = self.driver.find_element_by_id("1")
        ans3_to_q2 = self.driver.find_element_by_id("2A")
        ans3_to_q3 = self.driver.find_element_by_id("3A")
        ans3_to_q4 = self.driver.find_element_by_id("4")
        ans3_to_q5 = self.driver.find_element_by_id("5")
        submit_t3 = self.driver.find_element_by_id("submit")

        ans3_to_q1.send_keys("10")
        ans3_to_q2.click()
        ans3_to_q3.click()
        ans3_to_q4.send_keys("4")
        ans3_to_q5.send_keys("4")
        submit_t3.click()
        self.driver.implicitly_wait(5)

        self.driver.get('http://127.0.0.1:5000/stats')
        score_to_q1 = self.driver.find_element_by_id("yourNum").text
        self.assertEqual(score_to_q1, "20%")

        test2_button = self.driver.find_element_by_id("test2")
        test2_button.click()
        score_to_q2 = self.driver.find_element_by_id("yourNum").text
        self.assertEqual(score_to_q2, "80%")

        test3_button = self.driver.find_element_by_id("test3")
        test3_button.click()
        score_to_q3 = self.driver.find_element_by_id("yourNum").text
        self.assertEqual(score_to_q3, "40%")


    
    def test_login(self):
        self.driver.get('http://127.0.0.1:5000/sign-up')
        self.driver.implicitly_wait(5)
        eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-')
        print('event id is', eventid)
        time.sleep(1)
        user_signup_sheet = self.driver.find_element_by_id("username")
        user_signup_sheet.send_keys(eventid)
        self.driver.implicitly_wait(5)

        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('iLoveAgile')
        user_password_confirm = self.driver.find_element_by_id("passwordConfirm")
        user_password_confirm.send_keys('iLoveAgile')
        submit_button = self.driver.find_element_by_name("")
        submit_button.click()

        self.driver.get('http://127.0.0.1:5000/logout')   
        self.driver.implicitly_wait(5)
        # Login
        self.driver.get('http://127.0.0.1:5000/login')
        user_signup_sheet = self.driver.find_element_by_id("username")
        user_signup_sheet.send_keys(eventid)

        self.driver.implicitly_wait(5)

        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('iLoveAgile')

        submit_button2 = self.driver.find_element_by_name("")
        submit_button2.click()
        self.driver.implicitly_wait(5)

        self.assertEqual(self.driver.current_url,'http://127.0.0.1:5000/learn')
        self.assertNotEqual(self.driver.current_url,'http://127.0.0.1:5000/login')

        self.driver.get('http://127.0.0.1:5000/logout')  
        self.driver.implicitly_wait(5)
        # Login
        self.driver.get('http://127.0.0.1:5000/login')
        user_login_sheet = self.driver.find_element_by_id("username")
        user_login_sheet.send_keys(eventid)

        self.driver.implicitly_wait(5)

        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('iLoveAgileWebDev')

        submit_button3 = self.driver.find_element_by_name("")
        submit_button3.click()
        self.driver.implicitly_wait(5)
        self.assertEqual(self.driver.current_url,'http://127.0.0.1:5000/login')
        self.assertNotEqual(self.driver.current_url,'http://127.0.0.1:5000/learn')

        self.driver.implicitly_wait(5)
    
    def test_theme_change(self):
        # Make account
        self.driver.get('http://127.0.0.1:5000/sign-up')
        self.driver.implicitly_wait(5)
        eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-')
        print('event id is', eventid)
        user_signup_sheet = self.driver.find_element_by_id("username")
        user_signup_sheet.send_keys(eventid)
        self.driver.implicitly_wait(5)
        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('iLoveAgile')
        user_password_confirm = self.driver.find_element_by_id("passwordConfirm")
        user_password_confirm.send_keys('iLoveAgile')
        submit_button = self.driver.find_element_by_name("")
        submit_button.click()

        self.driver.get('http://127.0.0.1:5000/learn/test-1')
        ans1_to_q1 = self.driver.find_element_by_id("1B")
        ans1_to_q2 = self.driver.find_element_by_id("2A")
        ans1_to_q3 = self.driver.find_element_by_id("3B")
        ans1_to_q4 = self.driver.find_element_by_id("4B")
        ans1_to_q5 = self.driver.find_element_by_id("5")
        submit_t1 = self.driver.find_element_by_id("submit")

        ans1_to_q1.click()
        ans1_to_q2.click()
        ans1_to_q3.click()
        ans1_to_q4.click()
        ans1_to_q5.send_keys("4")
        submit_t1.click()
        self.driver.implicitly_wait(5)

        self.driver.get('http://127.0.0.1:5000/learn/test-2')
        ans2_to_q1 = self.driver.find_element_by_id("1A")
        ans2_to_q2 = self.driver.find_element_by_id("2A")
        ans2_to_q3 = self.driver.find_element_by_id("3B")
        ans2_to_q4 = self.driver.find_element_by_id("4A")
        ans2_to_q5 = self.driver.find_element_by_id("5A")
        submit_t2 = self.driver.find_element_by_id("submit")

        ans2_to_q1.click()
        ans2_to_q2.click()
        ans2_to_q3.click()
        ans2_to_q4.click()
        ans2_to_q5.click()
        submit_t2.click()
        self.driver.implicitly_wait(5)


        self.driver.get('http://127.0.0.1:5000/learn/test-3')
        ans3_to_q1 = self.driver.find_element_by_id("1")
        ans3_to_q2 = self.driver.find_element_by_id("2A")
        ans3_to_q3 = self.driver.find_element_by_id("3A")
        ans3_to_q4 = self.driver.find_element_by_id("4")
        ans3_to_q5 = self.driver.find_element_by_id("5")
        submit_t3 = self.driver.find_element_by_id("submit")

        ans3_to_q1.send_keys("2")
        ans3_to_q2.click()
        ans3_to_q3.click()
        ans3_to_q4.send_keys("20")
        ans3_to_q5.send_keys("20")
        submit_t3.click()
        self.driver.implicitly_wait(5)

        self.driver.get('http://127.0.0.1:5000/stats')

        green_theme = self.driver.find_element_by_id("Green")
        green_theme.click()
        time.sleep(1)

        Red_theme = self.driver.find_element_by_id("Red")
        Red_theme.click()    
        time.sleep(1)   

        Purple_theme = self.driver.find_element_by_id("Purple")
        Purple_theme.click()
        time.sleep(1)

        blue_theme = self.driver.find_element_by_id("Blue")
        blue_theme.click()
        time.sleep(1)
    
    def test_complete_operation(self):
        self.driver.get('http://127.0.0.1:5000/sign-up')
        self.driver.implicitly_wait(5)
        eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-')
        print('event id is', eventid)
        time.sleep(1)
        user_signup_sheet = self.driver.find_element_by_id("username")
        user_signup_sheet.send_keys(eventid)
        # time.sleep(10)
        self.driver.implicitly_wait(5)

        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('coolUser')
        user_password_confirm = self.driver.find_element_by_id("passwordConfirm")
        user_password_confirm.send_keys('coolUser')
        submit_button = self.driver.find_element_by_name("")

        submit_button.click()

        self.driver.get('http://127.0.0.1:5000/learn/test-1')
        ans1_to_q1 = self.driver.find_element_by_id("1A")
        ans1_to_q2 = self.driver.find_element_by_id("2A")
        ans1_to_q3 = self.driver.find_element_by_id("3A")
        ans1_to_q4 = self.driver.find_element_by_id("4A")
        ans1_to_q5 = self.driver.find_element_by_id("5")
        submit_t1 = self.driver.find_element_by_id("submit")

        ans1_to_q1.click()
        ans1_to_q2.click()
        ans1_to_q3.click()
        ans1_to_q4.click()
        ans1_to_q5.send_keys("5")
        submit_t1.click()
        self.driver.implicitly_wait(5)

        self.driver.get('http://127.0.0.1:5000/learn/test-2')
        ans2_to_q1 = self.driver.find_element_by_id("1A")
        ans2_to_q2 = self.driver.find_element_by_id("2A")
        ans2_to_q3 = self.driver.find_element_by_id("3A")
        ans2_to_q4 = self.driver.find_element_by_id("4A")
        ans2_to_q5 = self.driver.find_element_by_id("5A")
        submit_t2 = self.driver.find_element_by_id("submit")

        ans2_to_q1.click()
        ans2_to_q2.click()
        ans2_to_q3.click()
        ans2_to_q4.click()
        ans2_to_q5.click()
        submit_t2.click()
        self.driver.implicitly_wait(5)


        self.driver.get('http://127.0.0.1:5000/learn/test-3')
        ans3_to_q1 = self.driver.find_element_by_id("1")
        ans3_to_q2 = self.driver.find_element_by_id("2A")
        ans3_to_q3 = self.driver.find_element_by_id("3A")
        ans3_to_q4 = self.driver.find_element_by_id("4")
        ans3_to_q5 = self.driver.find_element_by_id("5")
        submit_t3 = self.driver.find_element_by_id("submit")

        ans3_to_q1.send_keys("10")
        ans3_to_q2.click()
        ans3_to_q3.click()
        ans3_to_q4.send_keys("4")
        ans3_to_q5.send_keys("4")
        submit_t3.click()
        self.driver.implicitly_wait(5)

        self.driver.get('http://127.0.0.1:5000/learn')
        time.sleep(2)

        self.driver.get('http://127.0.0.1:5000/logout')
   
        self.driver.implicitly_wait(5)
        # relogin
        self.driver.get('http://127.0.0.1:5000/login')
        user_signup_sheet = self.driver.find_element_by_id("username")
        user_signup_sheet.send_keys(eventid)

        self.driver.implicitly_wait(5)

        user_password = self.driver.find_element_by_id("password")
        user_password.send_keys('coolUser')

        submit_button2 = self.driver.find_element_by_name("")
        submit_button2.click()
        self.driver.implicitly_wait(5)

        self.driver.get('http://127.0.0.1:5000/stats')
        score_to_q1 = self.driver.find_element_by_id("yourNum").text
        self.assertEqual(score_to_q1, "20%")

        test2_button = self.driver.find_element_by_id("test2")
        test2_button.click()
        score_to_q2 = self.driver.find_element_by_id("yourNum").text
        self.assertEqual(score_to_q2, "80%")

        test3_button = self.driver.find_element_by_id("test3")
        test3_button.click()
        score_to_q3 = self.driver.find_element_by_id("yourNum").text
        self.assertEqual(score_to_q3, "40%")        



if __name__ =='__main__':
    unittest.main(verbosity=2)
