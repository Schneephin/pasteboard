#!/usr/bin/env python
import cgi, sys
from lib import *
import json

form = cgi.FieldStorage() 
token = form.getvalue('tk')
cookie = cookie.Cookie()
c = cookie.get("tk")

if not token and not c or c == "None" or token == "None":
    basics.forbidden()
else:
    if not c or (token and  not c == token) :
        #set toke to cookie
        print(cookie.set("tk",token))

    header ={}
    header['Content-type'] = 'text/html'
    basics.print_headers(header)
    #get layout
    template = "layout.html.tpl"
    tpl = "".join(open(template,'r').readlines())
    
    #define templates to load
    pages = {'header': 'headerloggedin','footer':'footer','content':'pastes','sidebar':'sidenav'}

    #print page
    sys.stdout.write(tpl.format(str(json.dumps(pages))))
