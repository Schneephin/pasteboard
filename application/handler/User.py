from application.db import *


class User:
    def __init__(self):
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
        user = User.User()
        return user.createUser(key)

