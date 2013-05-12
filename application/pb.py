
from application.handler import *

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


