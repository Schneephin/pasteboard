#!/usr/bin/env python

import cgi, sys
from lib import *
import json

# get token from request and cookie
form = cgi.FieldStorage() 
token = form.getvalue('tk')
cookie = cookie.Cookie()
c = cookie.get("tk")

# if no token is given use forbidden function to redirect to start page
if not token and not c or c == "None" or token == "None":
    basics.forbidden()
else:
    # if token is post but not in cookie write cookie
    if not c or (token and  not c == token) :
        #set token to cookie
        print(cookie.set("tk",token))

    #get layout
    template = "layout.html.tpl"
    tpl = "".join(open(template,'r').readlines())
    
    #define templates to load
    pages = {'header':'headerloggedin','footer':'footer','content':'pastes','sidebar':'sidenav'}
    
    # print header
    basics.print_headers({'Content-type':'text/html'})
    # print page including pages variable
    sys.stdout.write(tpl.format(str(json.dumps(pages))))
