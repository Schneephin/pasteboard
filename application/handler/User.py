from application.db.User import User as dbUser
from application.db.Token import Token as dbToken


class User:
    """
        User: 
        User-handler class handles all requests for user
        this class know witch db - handler class to use to
        get or set data to db

        @package application/handler
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
    def __init__(self):
        """
            __init__ 
            creates class-vars dbUser and dbToken

            @author Anja Siek <anja.marita@web.de> 
            @access private
        """
        self.dbUser = dbUser()
        self.dbToken = dbToken()


    def getInviteKey(self):
        """
            getInviteKey 
            create user with key on success return key 

            @author Anja Siek <anja.marita@web.de> 
            @access public
        """
        key = self.dbToken.generate_hash()
        self.createUser(key)

        return key

    def createUser(self,key):
        """
            createUser 
            call db-userobject to create an User with invitekey

            @author Anja Siek <anja.marita@web.de> 
            @param key key 
            @access public
        """
        self.dbUser.createUser(key)

    def register(self, uname, email, passw, ikey):
        """
            register 
            call db-userobject to register a new user

            @author Anja Siek <anja.marita@web.de> 
            @param uname uname 
            @param email email 
            @param passw passw 
            @param ikey ikey 
            @access public
        """
        uid = self.dbUser.register(uname, email, passw, ikey)
        token = self.dbToken.createToken(uid)  

        return token

    def login(self, email, passwd):
        """
            login 
            call db-user object to login an User

            @author Anja Siek <anja.marita@web.de> 
            @param email email 
            @param passwd passwd 
            @access public
        """
        uid = self.dbUser.login(email,passwd)
        token = self.dbToken.createToken(uid)  
        
        return token

    def getUser(self, token):
        """
            getUser 
            return an userobject by token

            @author Anja Siek <anja.marita@web.de> 
            @param token token 
            @access public
        """
        uid = self.dbToken.getUserIdbyToken(token)
        user = self.dbUser.getUserData(uid)
        return user
