# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

from config import RADIO, BARNA
from mpd_conn import dec_vol, inc_vol, init, play, stop

app = Flask("RadioControl")

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
    
    return render_template("index.html",
                           RADIO=RADIO, BARNA=BARNA);
    

if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0', debug=True)
