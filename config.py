import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask.ext.sqlalchemy import SQLAlchemy


SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
DEBUG = True
USERNAME = 'admin@gmail.com'
PASSWORD = 'lab336'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

'''
SQLALCHEMY_DATABASE_URI = \
    'mysql://ACCOUNT:PASSWORD@gardenia.csie.ntu.edu.tw/test'
'''
SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'share.sqlite')
