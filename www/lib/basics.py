#!/usr/bin/env python
"""
    basic lib file for functions needed in webpage (www)
    @author Anja Siek <anja.marita@web.de>
"""

import sys
from lib import cookie

def print_headers(headers):
    """
        print_headers 
        function to print all headers
        
        @author Anja Siek <anja.marita@web.de> 

        @param headers headers 
        @access public
    """
    for k, v in headers.items():
        sys.stdout.write('%s: %s\r\n' % (k, v))
    sys.stdout.write('\r\n')


def forbidden():
    """
        forbidden function redirects to start page 
        and returns 403 forbidden http error
        also removes token - cookie
        @author Anja Siek <anja.marita@web.de>
        @access public
    """
    header ={}
    header['Location'] = 'index.py'
    print_headers(header)
