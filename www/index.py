#!/usr/bin/env python
import cgi, sys
from lib import *
import json

#get layout
template = "layout.html.tpl"
tpl = "".join(open(template,'r').readlines())
#define templates to load
pages = {'header': 'header','footer':'footer','content':'home'}

#print page
basics.print_headers({'Content-type':'text/html'})
sys.stdout.write(tpl.format(str(json.dumps(pages))))
