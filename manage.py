#!/usr/bin/env python
import os
import redis
import time
from app import create_app
from flask.ext.script import Manager, prompt_bool
from jinja2 import Environment, FileSystemLoader


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
manager = Manager(app)


@manager.command
def initdb():
    '''Creates all database tables.'''
    db.create_all()


@manager.command
def dropdb():
    '''Drops all database tables.'''
    if prompt_bool('Are you sure to drop your databse?'):
        db.drop_all()

if __name__ == '__main__':
    manager.run()
