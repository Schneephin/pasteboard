#!/usr/bin/env python
import cgi, sys
from lib import *
import json

cookie = cookie.Cookie()
c = cookie.get("tk")

if c and not c == "None":
    header ={}
    header["Location"] = 'pastes.py'
    header['Content-type'] = 'text/html; charset=utf-8'
    basics.print_headers(header)
else:
    #get layout
    template = "layout.html.tpl"
    tpl = "".join(open(template,'r').readlines())
    #define templates to load
    pages = {'header': 'header','footer':'footer','content':'home'}

    #print page
    basics.print_headers({'Content-type':'text/html'})
    sys.stdout.write(tpl.format(str(json.dumps(pages))))
