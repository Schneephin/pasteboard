
from application.handler import *
from application.db.User import DbUserError
from application.db.Token import DbTokenError

class PasteboardError(Exception):
    """
        DbUserError(Exception): 
        Exception for User-Db Class
        
        @package application 
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        """
            __str__ 
            to String method
            @author Anja Siek <anja.marita@web.de>
            @access private
        """
        return repr(self.value)

class Pb:
    """
        Pb: 
        main pasteboard class this is the application enty-point
        @package application
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
    def __init__(self):
        """
            __init__ 
            constructor
            @access private
        """
        pass

    def login(self, email, password):
        """
            login 
            get the correct handler and call the login-function
            @param email email 
            @param password password 
            @access public
        """
        user = User.User()
        return user.login(email, password)

    def getInviteKey(self):
        """
            getInviteKey 
            get the correct handler and call the Invite-key generation function
            @access public
        """
        user = User.User()
        return user.getInviteKey()

    def register (self, uname, email, passw, ikey):
        """
            register 
            get the correct handler and call the register function
            @param uname uname 
            @param email email 
            @param passw passw 
            @param ikey ikey 
            @access public
        """
        user = User.User()
        return user.register(uname, email, passw, ikey)

    def getUser(self,token):
        try:
            user = User.User()
            return user.getUser(token)
        except DbTokenError as e:
            raise PasteboardError(e.__str__()) 


