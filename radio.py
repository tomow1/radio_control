# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

from config import RADIO, BARNA
from mpd_conn import dec_vol, inc_vol, play, stop

app = Flask("RadioControl")

@app.route('/', methods=['GET'])
def index():
    #print("method: ", request.method)
    if request.args.has_key('action'):
        if request.args['action'] == 'play':
            #print "Now listening to: " + request.args['playlist']
            play(request.args['playlist'])
        elif request.args['action'] == 'stop':
            #print "Stopping playback"
            stop()
        elif request.args['action'] == 'inc_vol':
            #print "Increasing volume"
            inc_vol()
        elif request.args['action'] == 'dec_vol':
            #print "Decreasing volume"
            dec_vol()
        
    
    return render_template("index.html",
                           RADIO=RADIO, BARNA=BARNA);
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
