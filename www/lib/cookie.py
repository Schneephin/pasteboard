#!/usr/bin/env python
"""
    cookie lib for use in webpage (www)
    @author Anja Siek <anja.marita@web.de>
"""

import sys, os
import http.cookies 
import time

class Cookie():

    """
        Cookie(): Class for handle cookies
        
        @package lib 
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
    def set(self,key,value):
        """
            set key, value cookie pair 
            
            @author Anja Siek <anja.marita@web.de> 
            @param strine key 
            @param string value 
            @access public
        """
        headers = {}
        cookie = http.cookies.SimpleCookie()
        cookie[key] = value
        cookie[key]['expires'] = 86400
        return cookie

    def get(self,key):
        """
            get value for key from cookie 
            
            @author Anja Siek <anja.marita@web.de> 
            @param key key 
            @access public
        """
        try:
            c = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
            value = c[key].value
            return value
        except (http.cookies.CookieError, KeyError):
            return None 

    def delete(self,key):
        """
            delete cookie function 

            @author Anja Siek <anja.marita@web.de> 
            @param key key 
            @access public
        """
        if self.get(key):
            headers = {}
            cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
            cookie[key] = ""
            cookie[key]['expires'] = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(time.time()))
            return cookie
