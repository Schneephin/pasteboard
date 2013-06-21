#!/usr/bin/env python
"""
    paste page 
    first entry point of paste page
    @author Anja Siek <anja.marita@web.de>
"""

import cgi, sys
from lib import *
import json

# get cookie to check token
cookie = cookie.Cookie()
c = cookie.get("tk")

if not c or c == "None":
    basics.forbidden()
else:
    #get layout
    template = "layout.html.tpl"
    tpl = "".join(open(template,'r').readlines())
    
    #define templates to load
    pages = {'header': 'headerloggedin','footer':'footer','content':'paste','sidebar':'sidenav'}

    # print header
    basics.print_headers({'Content-type':'text/html'})
    # print page including pages variable
    sys.stdout.write(tpl.format(str(json.dumps(pages))))

