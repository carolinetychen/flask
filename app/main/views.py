import os
import redis
import time
from flask import render_template, session, redirect, url_for, current_app
from flask import flash
from . import main
from .forms import LoginForm, BoardForm

User = 'user'
timeset = 'time'
valueset = 'comment'


def timeToDate(timestamp):
    timetuple = time.gmtime(timestamp)
    timestring = time.strftime("%Y-%m-%d %H:%M:%S", timetuple)
    return timestring


def getEntries(redis_db):
    entries = []
    time_ents = redis_db.zrange(timeset, 0, -1, withscores=True)

    for time_ent in time_ents:
        timestring = timeToDate(time_ent[1])
        valset = redis_db.smembers(time_ent[0])
        for val in valset:
            entries.append([time_ent[0], timestring, val])
    return entries


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        account = form.account.data
        password = form.password.data
        session['name'] = form.name.data
        currentAccount = current_app.config['USERNAME']
        currentPassword = current_app.config['PASSWORD']
        # 'Invalid account'
        if account != currentAccount or password != currentPassword:
            session['known'] = False
            flash('Invalid account or password')
        else:
            session['known'] = True
            return redirect(url_for('.board'))
        form.name.data = ''
        return render_template('index.html',
                               form=form, name=session.get('name'),
                               known=session.get('known'))
    session['known'] = False
    return render_template('index.html',
                           form=form,
                           known=session.get('known'))


@main.route('/board', methods=['GET', 'POST'])
def board():
    redis_db = redis.Redis(host='localhost', port=6379, db=0)

    board = BoardForm()
    entries = getEntries(redis_db)

    path = os.path.expanduser("~/Desktop/test")
    f = open(path, "r")
    count = 0

    for line in f:
        count += 1
        if redis_db.get("id") is None or count > int(redis_db.get("id")):
            s = line.split(" ")
            timestamp = float(s[0])
            text = int(s[1])

            name = session.get('name')
            uid = redis_db.incr("id")
            redis_db.zadd(timeset, "%d" % uid, timestamp)
            redis_db.sadd("%d" % uid, text)
        entries = getEntries(redis_db)

    return render_template('board.html', form=board, name=session.get('name'),
                           known=session.get('known', True),
                           entries=entries)
