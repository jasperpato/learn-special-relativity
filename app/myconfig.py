import os
basedir = os.path.abspath(os.path.dirname(__file__))

class MyConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'admin'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS  = False