#!/usr/bin/env python
import cgi, sys
from lib import *
import json

form = cgi.FieldStorage() 
token = form.getvalue('tk')
if not token:
    #redirect to start-page if toke is not set
    print("Status: 403 Forbidden")
    print("Refresh: 0; url=/")
    print()
    print("Redirecting ...")
else :
    #set toke to cookie
    cookie = cookie.Cookie()
    cookie.set("tk",token)
    
    #get layout
    template = "layout.html.tpl"
    tpl = "".join(open(template,'r').readlines())
    
    #define templates to load
    pages = {'header': 'headerloggedin','footer':'footer','content':'loggedin','sidebar':'sidenav'}

    #print page
    sys.stdout.write(tpl.format(str(json.dumps(pages))))
