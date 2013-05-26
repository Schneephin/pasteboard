from application.db.User import User as dbUser
from application.db.Token import Token as dbToken


class User:
    """
        User: 
        User-handler class  
        @package application
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
    def __init__(self):
        # create class-var DB-User
        self.dbUser = dbUser()
        self.dbToken = dbToken()


    def getInviteKey(self):
        """
            getInviteKey 
            create user with key on success return key 
            @access public
        """
        key = self.dbToken.generate_hash()
        self.createUser(key)

        return key

    def createUser(self,key):
        """
            createUser 
            call db-userobject to create an User with invitekey
            @param key key 
            @access public
        """
        self.dbUser.createUser(key)

    def register(self, uname, email, passw, ikey):
        """
            register 
            call db-userobject to register a new user
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
            @param email email 
            @param passwd passwd 
            @access public
        """
        uid = self.dbUser.login(email,passwd)
        token = self.dbToken.createToken(uid)  
        
        return token

    def getUser(self, token):
        uid = self.dbToken.getUserIdbyToken(token)
        user = self.dbUser.getUserData(uid)
        return user

