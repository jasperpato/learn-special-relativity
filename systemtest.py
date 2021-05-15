import unittest, os, time
from app import app, db 
from app.models import User, TestAttempt
from selenium import webdriver

class SystemTest(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'        
        db.create_all() 
    






if __name__ =='__main__':
    unittest.main(verbosity=2)