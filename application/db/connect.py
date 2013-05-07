#!/usr/bin/python
# -*- coding: utf-8 -*-

import oursql as mdb 


class DB():

    def __init__(self):
        self.connection = None
        self.config = {
            'host': "localhost",
            'user': "pasteboard",
            'pass': "pasteboard",
            'db':   "pasteboard"
        } 

    def connect(self):
        try:
            self.connection = mdb.connect(
                host = self.config['host'], 
                db = self.config['db'], 
                user = self.config['user'], 
                passwd = self.config['pass'],
            )
            
        except mdb.Error as e:
            return  "Error %d: %s" % (e.args[0], e.args[1])

    def getConnection(self):
        if not self.connection:
            self.connect()
        return self.connection


    def disconnect(self):
        
        if self.connection:
            self.connection.close()

