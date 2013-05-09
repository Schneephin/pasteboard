from application.db.User import User as dbUser


class User:
    def __init__(self):
        self.dbUser = dbUser()
        pass


    def generate_hash(self):
        """
            generate_hash 
            function to generate hash-key 
            @access public
        """
        import hashlib, time
        return hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()

    def getInviteKey(self):
        key = self.generate_hash()
        self.createUser(key)

        return key

    def createUser(self,key):
        self.dbUser.createUser(key)

    def register(self, uname, email, passw, ikey):
        self.dbUser.register(uname, email, passw, ikey)

        return self.generate_hash()

    def login(self, email, passwd):
        self.dbUser.login(email,passwd)
        
        return self.generate_hash()



