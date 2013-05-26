#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql as mdb 

class DB():

    """
        DB(): 
        abstract db class with connection information 

        @package application
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
    def __init__(self):
        """
            __init__ 
            constructor function set configuration 
            @todo: put it into config-file
            @access private
        """
        self.mdb = mdb
        self.connection = None
        self.config = {
            'host': "localhost",
            'user': "pasteboard",
            'pass': "pasteboard",
            'db':   "pasteboard"
        } 

    def connect(self):
        """
            connect 
            try to connet to db  
            @access public
        """
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
        """
            getConnection 
            return a db-connection object
            @access public
        """
        if not self.connection:
            self.connect()
        return self.connection


    def disconnect(self):
        """
            disconnect 
            close connection if exists
            @access public
        """
        
        if self.connection:
            self.connection.close()

