from application.db.Paste import Paste as dbPaste


class Paste:
    """
        Paste: 
        Paste-handler class  
        @package application
        @version $id$
        @author Christian Wenzlick <christian.wenzlick@siemens.com> 
    """
    def __init__(self):
        # create class-var DB-Paste
        self.dbPaste = dbPaste()

    def createNewPaste(self, parent_id, category_id, user_id, paste_content, title):
        """
            createNewPaste
            function to create a new paste
            @param parent_id Id of this pastes parent
            @param category_id Category Id for this paste
            @param user_id Id of the creating user
            @param paste_content Content of the paste
            @param title Title of the paste
            @access public
        """
        
        paste_id = self.dbPaste.createNewPaste(parent_id, category_id, user_id, paste_content, title)    
        
        return paste_id
        
    def getAllPastesByUser(self, user_id):
        """
            getAllPastesByUser 
            function to get all pastes created by a specific user
            @param user_id Id of the user
            @access public
        """
        
        pastes = self.dbPaste.getAllPastesByUser(user_id)
        
        return pastes
        
    def getAllChildPastes(self, paste_id):
        """
            getAllChildPastes 
            function to get all child pastes of a specific paste
            @param paste_id Id of the paste
            @access public
        """
        
        pastes = self.dbPaste.getAllChildPastes(paste_id)
        
        return pastes
    
    def getAllPastesByCategory(self, category_id):
        """
            getAllPastesByCategory 
            function to get all pastes in a category
            @param category_id ID of the category
            @access public
        """
        
        pastes = self.dbPaste.getAllPastesByCategory(category_id)
                
        return pastes
        
    def getPasteByID (self, paste_id):
        """
            getPasteByID 
            function to get a paste by id
            @param paste_id id of the paste
            @access public
        """
        
        paste = self.dbPaste.GetPasteByID(paste_id)
        
        return paste
        
    def editPaste(self, paste_id, parent_id, category_id, user_id, paste_content, title):
        """
            editPaste
            function to edit a paste
            @param paste_id Id of the paste
            @param parent_id Id of this pastes parent
            @param category_id Category Id for this paste
            @param user_id Id of the editing user
            @param paste_content Content of the paste
            @param title Title of the paste
            @access public
        """
            
        self.dbPaste.editPaste(paste_id, parent_id, category_id, user_id, paste_content, title)    
    
        
        
        
    
