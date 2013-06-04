#!/usr/bin/env python
import cgi, sys
from lib import *
import json

cookie = cookie.Cookie()
c = cookie.get("tk")

if c and not c == "None":
    #if is logged in use different templates
    pages = {'header': 'headerloggedin','footer':'footer','content':'about'}
else:
    pages = {'header': 'header','footer':'footer','content':'about'}

#get layout
template = "layout.html.tpl"
tpl = "".join(open(template,'r').readlines())

#print page
basics.print_headers({'Content-type':'text/html'})
sys.stdout.write(tpl.format(str(json.dumps(pages))))
