#!/usr/bin/env python
"""
    index (home) page 
    first entry point of webpage
    @author Anja Siek <anja.marita@web.de>
"""

import cgi, sys
from lib import *
import json

# get cookie
cookie = cookie.Cookie()
c = cookie.get("tk")

# check cookie exists
if c and not c == "None":
    # if cookie token exists and is not None 
    # redirect to pastes.py page
    header ={}
    header["Location"] = 'pastes.py'
    header['Content-type'] = 'text/html; charset=utf-8'
    basics.print_headers(header)
else:
    # get layout
    template = "layout.html.tpl"
    tpl = "".join(open(template,'r').readlines())

    # define templates to loaded this will be pushed into pageHandle function in template 
    pages = {'header': 'header','footer':'footer','content':'home'}

    # print header
    basics.print_headers({'Content-type':'text/html'})
    # print page including pages variable
    sys.stdout.write(tpl.format(str(json.dumps(pages))))
