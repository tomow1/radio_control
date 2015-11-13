# -*- coding: utf-8 -*-
from mpd import MPDClient
from config import MPD_SRV

srv = MPDClient()
volume = 76

def conn(func):
    def wrapper(*args):
        srv.connect(MPD_SRV['host'], MPD_SRV['port'])
        srv.password(MPD_SRV['passwd'])
        func(*args)
        srv.disconnect()

    return wrapper

@conn
def init():
    global volume
    srv.repeat(1)
    srv.setvol(volume)

@conn
def dec_vol():
    global volume
    if volume > 50:
        volume -= 2
        srv.setvol(volume)
        print "volume dereased to " + str(volume)
    else:
        print "volume at minimum"

@conn
def inc_vol():
    global volume
    if volume < 100:
        volume += 2
        srv.setvol(volume)
        print "volume inreased to " + str(volume)
    else:
        print "volume at maximum"

@conn
def play(playlist):
    srv.clear()
    srv.load(playlist)
    srv.play(0)

@conn
def stop():
    srv.stop()
    srv.clear()
