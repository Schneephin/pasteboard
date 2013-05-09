
from application.handler import *

class Pb:
    def __init__(self):
        pass

    def login(self, email, password):
        user = User.User()
        return user.login(email, password)

    def getInviteKey(self):
        user = User.User()
        return user.getInviteKey()

    def register (self, uname, email, passw, ikey):
        user = User.User()
        return user.register(uname, email, passw, ikey)


