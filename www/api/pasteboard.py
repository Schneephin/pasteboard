#!/usr/bin/env python
"""
    pasteboard.py
    api for pasteboard-application
    @author Anja Siek <anja.marita@web.de>
    @author Christian Wenzlick <christian.wenzlick@siemens.com>
"""

# some imports
import cgi, os, sys
import cgitb; cgitb.enable()
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from application.pb import Pb
from application.pb import PasteboardError


class Pasteboard:

    """
        Pasteboard: 
        Api class for pasteboard-application
        
        @package pasteboard 
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
    def __init__(self,data):
        """
            __init__ 
            create class-vars data and pb 
            @param data data 
            @access private
        """
        self.data = data
        self.pb = Pb()

    def login(self):
        """
            login 
            ligin wit email and password

            @author Anja Siek <anja.marita@web.de> 
            @access public
        """
        # get POST Data
        email = cgi.escape(json.loads(self.data)['email'])
        passwd = cgi.escape(json.loads(self.data)['password'])

        #some basic validations
        if not email or not passwd:
            result = {'state': 'error'}
            result['msg'] = 'email or password is wrong'
        else:
            try :
                # if login was success it will return a login-token
                token = self.pb.login(email,passwd)
                result = {'state': 'ok'}
                result['data'] = {'token': token }
            except Exception as e:
                result = {'state': 'error'}
                result['msg'] = e.__str__()

        self.return_response(result)


    def getUser(self):
        """
            getUser 
            get user from application
            
            @author Anja Siek <anja.marita@web.de> 
            @access public
        """
        token = cgi.escape(json.loads(self.data)['tk'])
        result = {'state': 'error'}

        try :
            user = self.pb.getUser(token)
            result = {'state': 'ok'}
            result['data'] = user 
        except PasteboardError as e:
            result['msg'] = e.__str__()
            pass
        except Exception as e:
            result['msg'] = e.__str__()
        
        self.return_response(result)

    def getPastesList(self):
        """
            getPastesListByUser 
            get a list of all paste in a category
            @author Anja Siek <anja.marita@web.de> 
            @author Christian Wenzlick <christian.wenzlick@siemens.com>
            @access public
        """
        token = cgi.escape(json.loads(self.data)['tk'])
        catid = int(cgi.escape(json.loads(self.data)['cat']))
        if not catid:
            catid = 0
        
        if self.checkToken(token):
            
            result = {'state': 'ok'}
            result['data'] = {
                'pastes': self.pb.getAllPastesByCategory(catid)
            
            }
            self.return_response(result)
        else:
            self.print_headers({"Status": "403 Forbidden"})
    
    def getPasteById(self):
        """
           getPasteById
           get a paste with a given id
           @author Christian Wenzlick <christian.wenzlick@siemens.com>
           @access public
        """   
        paste_id = cgi.escape(json.loads(self.data)['paste_id'])   
        if not paste_id:
            result = {'state': 'error'} 
            result['msg'] = 'no paste id'       
        else:
            try:
                paste = self.pb.getPasteById(paste_id)
                sys.stderr.write(paste.__str__())
                result = {'state': 'ok'}
                result['data'] = {'paste': paste }
            except Exception as e:
                result = {'state': 'error'}
                result['msg'] = e.__str__()
           
        self.return_response(result)           

    def createPaste(self):
        """
            createPaste 
            create a new paste
            @author Christian Wenzlick <christian.wenzlick@siemens.com> 
            @access public
        """
        parent_id = cgi.escape(json.loads(self.data)['parent'])   
        category_id = cgi.escape(json.loads(self.data)['category'])
        user_id = cgi.escape(json.loads(self.data)['userid']) 
        paste_content = cgi.escape(json.loads(self.data)['codeMirrorEditor'])
        title = cgi.escape(json.loads(self.data)['title'])		
 
        if not parent_id:
            parent_id = 0
        if not category_id:    
            category_id = 0
            
        if not paste_content:
            result = {'state': 'error'} 
            result['msg'] = 'no paste content'       
        elif not user_id:
            result = {'state': 'error'}
            result['msg'] = 'invalid user'
        elif not title:
            result = {'state': 'error'}
            result['msg'] = 'no title'
        else:
            try:
                paste_id = self.pb.createNewPaste(parent_id, category_id, user_id, paste_content, title)
                result = {'state': 'ok'}
                result['data'] = {'paste_id': paste_id }
            except Exception as e:
                result = {'state': 'error'}
                result['msg'] = e.__str__()
            
        self.return_response(result)
   
    def getInviteKey(self):
        """
            getInviteKey 
            return a new invitekey for registration
            
            @author Anja Siek <anja.marita@web.de> 
            @access public
        """
        
        key = self.pb.getInviteKey()

        result = {'state': 'ok'}
        result['data'] = {'invkey': key}
        self.return_response(result)

    def register(self):
        """
            register 
            function to register a new user

            @author Anja Siek <anja.marita@web.de> 
            @access public
        """
        # get POST Data
        email = cgi.escape(json.loads(self.data)['email'])
        name = cgi.escape(json.loads(self.data)['name'])
        passwd = cgi.escape(json.loads(self.data)['password'])
        passwdr = cgi.escape(json.loads(self.data)['password-r'])
        key = cgi.escape(json.loads(self.data)['key'])

        # some bsic validations
        if not passwd or not passwdr or not (passwd == passwdr):
            result = {'state': 'error'} 
            result['msg'] = 'your password is wrong'
        elif not email or not name or not key:
            result = {'state': 'error'}
            result['msg'] = 'email, name and invite key musst be set'
        else:
            try:
                # if we can save user in db it will return an login token
                token = self.pb.register(name, email, passwd, key)
                result = {'state': 'ok'}
                result['data'] = {'token': token }
            except Exception as e:
                result = {'state': 'error'}
                result['msg'] = e.__str__()

        self.return_response(result)

    def allCategorys(self):
        """
            allCategorys 
            get all categories 

            @author Anja Siek <anja.marita@web.de> 
            @access public
        """
        token = cgi.escape(json.loads(self.data)['tk'])
        result = {'state': 'error'}

        if self.checkToken(token):
            try :
                categorys = self.pb.getAllCategorys()
                result = {'state': 'ok'}
                result['data'] = {'categorys': categorys}
            except PasteboardError as e:
                self.print_headers({"Status": "403 Forbidden"})
                result['msg'] = e.__str__()
                pass
            except Exception as e:
                result['msg'] = e.__str__()
        else:
            self.print_headers({"Status": "403 Forbidden"})
        
        self.return_response(result)
 

        
    def checkToken(self,tk):
        """
            checkToken 
            check for token is valid
            
            @author Anja Siek <anja.marita@web.de> 
            @param tk tk 
            @access public
        """
        return True

    def return_response(self,result):
        """
            return_response 
            function to return the results
            
            @author Anja Siek <anja.marita@web.de> 
            @param result result 
            @access public
        """
        # return access-Token
        self.print_headers({"Content-Type": "text/html"})
        sys.stdout.write(json.dumps(self.convert_values_to_string(result),  default=str))

    def convert_values_to_string(self,dictionary):
        """Recursively converts dictionary keys to strings."""
        if isinstance(dictionary, bytes):
            return str(dictionary,"utf8")
        elif isinstance(dictionary, dict):
            return dict((str(k), self.convert_values_to_string(v)) 
                for k, v in dictionary.items())
        else:
            return dictionary

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
    """
        main 
        main method handles api-functions
       
        @author Anja Siek <anja.marita@web.de> 
        @access public
    """

    # get request-values
    form = cgi.FieldStorage()
    data = form.getvalue('data')
    # get api function called
    function = os.environ['PATH_INFO'].split("/")[1]
    # set request-values into api
    pasteboard = Pasteboard(data)

    # check if called api-function exists if yes call it
    # if not return with 404 not found
   # try:
    if function == 'login':
        pasteboard.login()
    elif function == 'getUser':
        pasteboard.getUser()
    elif function == 'getPastesList':
        pasteboard.getPastesList()
    elif function == 'getPasteById':
        pasteboard.getPasteById()
    elif function == 'getInviteKey':
        pasteboard.getInviteKey()
    elif function == 'createPaste':
        pasteboard.createPaste()
    elif function == 'register':
        pasteboard.register()
    elif function == 'getAllCategorys':
        pasteboard.allCategorys()
    else:
        pasteboard.print_headers({"Status": "404 Not found"})
   # except:
    #    pasteboard.print_headers({"Status": "404 Not found"})

if __name__ == '__main__':
    main()
