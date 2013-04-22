#!/usr/bin/env python

import sys, os, pickle
import http.cookies 
import basics


def generate_hash():
    import hashlib, time
    return hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()


def loadSession():
    if not os.path.exists('tmp/.sessions'):
        os.mkdir('tmp/.sessions')

    try:
        cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        sid = cookie["sid"].value
    except (http.cookies.CookieError, KeyError):
        sid = generate_hash()
        setToCockie('sid', str(sid).encode('utf-8'))

    if os.path.exists(os.path.join('.sessions', sid)):
        session_file = open(os.path.join('.sessions', sid), 'rb')
        session_obj = pickle.load(session_file)
        session_file.close()
    else:
        session_obj = {}

    session_file = open(os.path.join('.sessions', sid), 'wb')
    pickle.dump(session_obj, session_file, 1)
    session_file.close()



