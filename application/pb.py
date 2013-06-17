
from application.handler import *
from application.db.User import DbUserError
from application.db.Token import DbTokenError
from application.db.Paste import DbPasteError

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

    def getAllCategorys(self):
        cat = Categorys.Category()
        return cat.getAllCategorys()
    
    def getAllPastesByUser(self, user_id):
        """
            getAllPastesByUser 
            get all pastes created by a user
            @author: Christian Wenzlick
            @access public
        """
        try:
            paste = Paste.Paste()
            return paste.getAllPastesByUser(user_id)
        except DbPasteError as e:
            raise PasteboardError(e.__str__()) 
    
    def getAllChildPastes(self, paste_id):
        """
            getAllChildPastes 
            get all pastes which are children of a given paste
            @author: Christian Wenzlick
            @access public
        """
        try:
            paste = Paste.Paste()
            return paste.getAllChildPastes(paste_id)
        except DbPasteError as e:
            raise PasteboardError(e.__str__()) 
        
    def getAllPastesByCategory(self, category_id):
        """
            getAllPastesByCategory 
            get all pastes in a category
            @author: Christian Wenzlick
            @access public
        """
        try:
            paste = Paste.Paste()
            return paste.getAllPastesByCategory(category_id)
        except DbPasteError as e:
            raise PasteboardError(e.__str__()) 
    
    def getPasteById(self, paste_id):
        """
            getPasteById 
            get the paste with a given id
            @author: Christian Wenzlick
            @access public
        """
        try:
            paste = Paste.Paste()
            return paste.getPasteByID(paste_id)
        except DbPasteError as e:
            raise PasteboardError(e.__str__()) 
    
    def editPaste(self, paste_id, parent_id, category_id, user_id, paste_content, title):
        """
            editPaste 
            edit an existing paste
            @author: Christian Wenzlick
            @access public
        """
        try:
            paste = Paste.Paste()
            return paste.editPaste(paste_id, parent_id, category_id, user_id, paste_content, title)
        except DbPasteError as e:
            raise PasteboardError(e.__str__()) 
    
    def createNewPaste(self, parent_id, category_id, user_id, paste_content, title):
        """
            createNewPaste 
            create a new paste
            @author: Christian Wenzlick
            @access public
        """
        try:
            paste = Paste.Paste()
            return paste.createNewPaste(parent_id, category_id, user_id, paste_content, title)
        except DbPasteError as e:
            raise PasteboardError(e.__str__()) 
    
    