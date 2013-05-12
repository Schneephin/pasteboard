from application.db.User import User as dbUser


class User:
    def __init__(self):
    """
        User: 
        User-handler class  
        @package application
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
        # create class-var DB-User
        self.dbUser = dbUser()

    def generate_hash(self):
        """
            generate_hash 
            function to generate hash-key 
            @access public
        """
        import hashlib, time
        return hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()

    def getInviteKey(self):
        """
            getInviteKey 
            create user with key on success return key 
            @access public
        """
        key = self.generate_hash()
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
        self.dbUser.register(uname, email, passw, ikey)

        return self.generate_hash()

    def login(self, email, passwd):
        """
            login 
            call db-user object to login an User
            @param email email 
            @param passwd passwd 
            @access public
        """
        self.dbUser.login(email,passwd)
        
        return self.generate_hash()
