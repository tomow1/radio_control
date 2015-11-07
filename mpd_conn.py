# -*- coding: utf-8 -*-
from mpd import MPDClient
from config import MPD_SRV

srv = MPDClient()

#
# skal bli decorator
#
srv.connect(MPD_SRV['host'], MPD_SRV['port'])
srv.password(MPD_SRV['passwd'])
srv.repeat(1)
#srv.close()
#

#volume = srv.status()['volume']

def dec_vol():
    #volume = volume - 3
    srv.setvol(int(srv.status()['volume']) - 3)

def inc_vol():
    #volume = volume + 3
    srv.setvol(int(srv.status()['volume']) + 3)

def play(playlist):
    srv.clear()
    srv.load(playlist)
    srv.play(0)

def stop():
    srv.stop()
    srv.clear()
