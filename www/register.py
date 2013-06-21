#!/usr/bin/env python
"""
    register page 
    first entry point to register page
    @author Anja Siek <anja.marita@web.de>
"""

import cgi, sys
from lib import *
import json


# get layout
template = "layout.html.tpl"
tpl = "".join(open(template,'r').readlines())

# define templates to load
pages = {'header': 'header','footer':'footer','content':'register'}

# print header
basics.print_headers({'Content-type':'text/html'})
# print page including pages variable
sys.stdout.write(tpl.format(str(json.dumps(pages))))
