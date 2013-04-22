#!/usr/bin/env python

import sys

def print_headers(headers):
    """
        print_headers 
        function to print all headers
        
        @author Anja Siek <anja.marita@web.de> 

        @param headers headers 
        @access public
    """
    for k, v in headers.items():
        sys.stdout.write('%s: %s\n' % (k, v))
    sys.stdout.write('\n')

