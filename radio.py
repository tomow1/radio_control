# -*- coding: utf-8 -*-
import os
import sqlite3
from flask import Flask, render_template, request, g, flash, redirect, url_for
from config import RADIO, BARNA
from mpd_conn import dec_vol, inc_vol, init, play, stop

app = Flask("RadioControl")

app.config.update(
    DATABASE=os.path.join(app.root_path, 'radio.db'),
    SECRET_KEY='development key'
)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        g.db = connect_db()
    return g.db


@app.teardown_appcontext
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        sql = 'insert into stations (display_name, name) values (?,?)'
        for station in RADIO:
            db.execute(sql, [station["display_name"], station["name"]])
            db.commit()
        sql = 'select display_name, name from stations order by display_name'
        cur = db.execute(sql)
        result = cur.fetchall()
        print "stations table created"
        print str(len(result)) + ' rows added'


@app.route('/', methods=['GET'])
def index():
    if request.args.has_key('action'):
        if request.args['action'] == 'play':
            play(request.args['playlist'])
        elif request.args['action'] == 'stop':
            stop()
        elif request.args['action'] == 'inc_vol':
            inc_vol()
        elif request.args['action'] == 'dec_vol':
            dec_vol()

    db = get_db()
    db.row_factory = sqlite3.Row
    sql = 'select display_name, name from stations order by display_name'
    cur = db.execute(sql)
    stations = cur.fetchall()

    return render_template("index.html",
                           RADIO=stations, BARNA=BARNA);


@app.route('/add', methods=['POST'])
def add_station():
    sql = 'insert into stations (display_name, name) values (?, ?)'
    db = get_db()
    db.execute(sql, [request.form['display_name'], request.form['name']])
    db.commit()
    flash('New station was successfully added')
    return redirect(url_for('index'))


@app.route('/add', methods=['GET'])
def add_station_form():
    return render_template('add_station.html')


if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0', debug=True)
