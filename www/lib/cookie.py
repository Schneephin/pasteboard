#!/usr/bin/env python

import sys, os, pickle
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
        headers['Content-type'] = 'text/html'
        headers['Set-Cookie'] = key + '=%s;' % value
        print_headers(headers)

    def get(self,key):
        """
            get value for key from cookie 
            
            @author Anja Siek <anja.marita@web.de> 
            @param key key 
            @access public
        """
        cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        value = cookie[key].value
        return key
