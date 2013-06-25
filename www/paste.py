#!/usr/bin/env python
"""
    paste page 
    first entry point of paste page
    @author Anja Siek <anja.marita@web.de>
    @author Christian Wenzlick <christian.wenzlick@siemens.com>
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
    #if paste.py is called with an id parameter prepare to load the corresponding paste
    form = cgi.FieldStorage() 
    paste_id = form.getvalue('id')
    if paste_id:
        print(cookie.set("pasteid",paste_id))
       
    #get layout
    template = "layout.html.tpl"
    tpl = "".join(open(template,'r').readlines())
    
    #define templates to load
    pages = {'header': 'headerloggedin','footer':'footer','content':'paste'}

    # print header
    basics.print_headers({'Content-type':'text/html'})
    # print page including pages variable
    sys.stdout.write(tpl.format(str(json.dumps(pages))))

