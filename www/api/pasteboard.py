#!/usr/bin/env python
"""
    login.py
    api for Login with username and pssword
    @author Anja Siek <anja.marita@web.de>
"""

import cgi, os, sys
import cgitb; cgitb.enable()
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from application.pb import Pb


class Pasteboard:

    def __init__(self,data):
        self.data = data
        self.pb = Pb()

    def login(self):
        #get POST Data
        email = cgi.escape(json.loads(self.data)['email'])
        passwd = cgi.escape(json.loads(self.data)['password'])

        self.pb.login(email,passwd)

        # @TODO: check values
        # lookup on db and generate Token + timeout
        # dummydata :
        if not email or not passwd:
            result = {'state': 'error'}
            result['msg'] = 'email or password is wrong'
        else:
            #do stuff
            token = self.generate_hash()
            result = {'state': 'ok'}
            result['data'] = {'token': token }

        self.return_response(result)

    def generate_hash(self):
        """
            generate_hash 
            function to generate hash-key 
            @access public
        """
        import hashlib, time
        return hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()

    def getUser(self):
        token = cgi.escape(json.loads(self.data)['tk'])
        if self.checkToken(token):
            result = {'state': 'ok'}
            result['data'] = {
                'id': '12',
                'email': 'lol@lal.de',
                'name': 'dörte'
            }
            
            self.return_response(result)
        else:
            print_headers({"Status": "403 Forbidden"})

    def getPastesList(self):
        token = cgi.escape(json.loads(self.data)['tk'])
        if self.checkToken(token):
            result = {'state': 'ok'}
            result['data'] = {
                'pastes':[
                    {
                        'title': 'pasteboard-api',
                        'id': 1,
                        'date':'04.05.2013 11:22:17'
                    },
                    {
                        'title': 'pasteboard-home.html',
                        'id': 2,
                        'date':'02.05.2013 10:11:01'
                    }
                ]
            }
            self.return_response(result)
        else:
            print_headers({"Status": "403 Forbidden"})
   
    def getInviteKey(self):
        result = {'state': 'ok'}
        result['data'] = {'invkey': self.generate_hash()}
        self.return_response(result)
 

        
    def checkToken(self,tk):
        return True

    def return_response(self,result):
        # return access-Token
        self.print_headers({"Content-Type": "text/html"})
        sys.stdout.write(json.dumps(result))

    def print_headers(self,headers):
        """
            print_headers 
            function to print all headers
            
            @author Anja Siek <anja.marita@web.de> 

            @param headers headers 
            @access public
        """
        for k, v in headers.items():
            sys.stdout.write('%s: %s\n' % (k, v))
        sys.stdout.write('\n')

def main():
    form = cgi.FieldStorage()
    data = form.getvalue('data')
    function = os.environ['PATH_INFO'].split("/")[1]
    pasteboard = Pasteboard(data)

    
    try:
        if function == 'login':
            pasteboard.login()
        elif function == 'getUser':
            pasteboard.getUser()
        elif function == 'getPastesList':
            pasteboard.getPastesList()
        elif function == 'getInviteKey':
            pasteboard.getInviteKey()
        else:
            pasteboard.print_headers({"Status": "404 Not found"})
    except:
        pasteboard.print_headers({"Status": "404 Not found"})

if __name__ == '__main__':
    main()

