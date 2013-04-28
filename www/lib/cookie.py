#!/usr/bin/env python

import sys, os
import http.cookies 

from lib.basics import print_headers

class Cookie():

    """
    Cookie(): Class for handle cookies
    
    @package lib 
    @version $id$
    @copyright 
    @author Anja Siek <anja.marita@web.de> 
    @license 
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
