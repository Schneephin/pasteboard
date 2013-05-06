#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb 
import sys



class DB ():

    connection = None
    config = {
        'host': "localhost",
        'user': "pasteboard",
        'pass': "pasteboard",
        'db':   "pasteboard"
    } 

    def connect(self, host, db, user, password):
        try:
            self.connection = mdb.connect(
                self.config['host'], self.config['db'], self.config['user'], self.config['password'])
            
        except mdb.Error, e:
          
            return  "Error %d: %s" % (e.args[0], e.args[1])

    def getConnection(self):
        if not self.connection:
            self.connect()
        return self.connection


    def disconnect():
        
        if self.connection:
            self.connection.close()

