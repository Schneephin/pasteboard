#!/usr/bin/env python
import cgi, sys
from lib import *
import json


header ={}
header['Content-type'] = 'text/html'
basics.print_headers(header)
#get layout
template = "layout.html.tpl"
tpl = "".join(open(template,'r').readlines())

#define templates to load
pages = {'header': 'header','footer':'footer','content':'register'}

#print page
sys.stdout.write(tpl.format(str(json.dumps(pages))))
