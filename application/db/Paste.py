from application.db.connect import DB

class DbPasteError(Exception):
    """
        DbPasteError(Exception): 
        Exception for Paste-Db Class
    """
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class Paste(DB):
    """
        Paste(DB): 
        extends connect.DB class so that all functions from 
        connect.DB are available
        @package application
        @author Christian Wenzlick <christian.wenzlick@siemens.com> 
        @version $id$
    """
    def __init__(self):
        # call parent init-method
        super().__init__()
        
    def createNewPaste(self, group_id, parent_id, category_id, user_id, paste_content):
        """
            createNewPaste 
            function to create a new paste
            @param group_id Group Id for the new paste
            @param parent_id Id of this pastes parent
            @param category_id Category Id for this paste
            @param user_id Id of the creating user
            @param paste_content Content of the paste
            @access public
        """
        
        if not user_id:
            raise DbPasteError("No user ID submitted")
        if not paste_content:
            raise DbPasteError("No content submitted")

        self.getConnection()
        cursor  = self.connection.cursor()
                
        cursor.execute('INSERT INTO pb_pastes (group_id, parent_id, category_id, user_id)  VALUES (%i, %i, %i, %i)',(group_id, parent_id, category_id, user_id))
        paste_id = self.connection.insert_id()
        self.getConnection().commit()
        cursor.execute('INSERT INTO pb_pastescontent (paste_id, content, datum)  VALUES (%i, %s, date())',(paste_id, paste_content))
        self.getConnection().commit()
        self.disconnect()
        
        return paste_id

    def getAllPastesByUser(self, user_id):
        """
            getAllPastesByUser 
            function to get all pastes created by a specific user
            @param user_id Id of the user
            @access public
        """
        
        if not user_id:
            raise DbPasteError("No user ID submitted")
            
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute('''SELECT 
                        pb_pastes.id as paste_id,
                        pb_pastes.group_id as group_id,
                        pb_pastes.parent_id as parent_id,
                        pb_pastes.category_id as category_id,
                        pb_pastes.user_id as user_id,
                        pb_pastescontent.content as paste_content,
                        pb_pastescontetn.datum as datum
                    FROM pb_pastes JOIN pb_pastescontent ON pb_pastes.id = pb_pastescontent.paste_id 
                    WHERE pb_pastes.user_id = %i''',user_id)
        pastes = cursor.fetchall()
        self.getConnection().commit()
        self.disconnect()

        return pastes
    
    def getAllChildPastes(self, paste_id):
        """
            getAllChildPastes 
            function to get all child pastes of a specific paste
            @param paste_id Id of the paste
            @access public
        """
        if not paste_id:
            raise DbPasteError("No paste ID submitted")
        
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute('''    SELECT 
                            pb_pastes.id as paste_id,
                            pb_pastes.group_id as group_id,
                            pb_pastes.parent_id as parent_id,
                            pb_pastes.category_id as category_id,
                            pb_pastes.user_id as user_id,
                            pb_pastescontent.content as paste_content,
                            pb_pastescontetn.datum as datum
                        FROM pb_pastes JOIN pb_pastescontent ON pb_pastes.id = pb_pastescontent.paste_id 
                        WHERE pb_pastes.parent_id = %i''',paste_id)
        pastes = cursor.fetchall()
        self.getConnection().commit()
        self.disconnect()
        
        return pastes
    
    def getAllPastesByCategory(self, category_id):
        """
            getAllPastesByCategory 
            function to get all pastes in a category
            @param category_id ID of the category
            @access public
        """
        if not category_id:
            raise DbPasteError("No category ID submitted")
        
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute('''    SELECT 
                            pb_pastes.id as paste_id,
                            pb_pastes.group_id as group_id,
                            pb_pastes.parent_id as parent_id,
                            pb_pastes.category_id as category_id,
                            pb_pastes.user_id as user_id,
                            pb_pastescontent.content as paste_content,
                            pb_pastescontetn.datum as datum
                        FROM pb_pastes JOIN pb_pastescontent ON pb_pastes.id = pb_pastescontent.paste_id 
                        WHERE pb_pastes.category_id = %i''',category_id)
        pastes = cursor.fetchall()
        self.getConnection().commit()
        self.disconnect()
        
        return pastes
    
    def getPasteByID (self, paste_id):
        """
            getPasteByID 
            function to get a paste by id
            @param paste_id id of the paste
            @access public
        """
        if not paste_id:
            raise DbPasteError("No paste ID submitted")
        
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute('''SELECT 
                    pb_pastes.id as paste_id,
                    pb_pastes.group_id as group_id,
                    pb_pastes.parent_id as parent_id,
                    pb_pastes.category_id as category_id,
                    pb_pastes.user_id as user_id,
                    pb_pastescontent.content as paste_content,
                    pb_pastescontetn.datum as datum
                FROM pb_pastes JOIN pb_pastescontent ON pb_pastes.id = pb_pastescontent.paste_id 
                WHERE pb_pastes.id = %i''',paste_id)
        paste = cursor.fetchone()
        
        if not paste:
            raise DbPasteError("No paste found for this ID")
        
        self.getConnection().commit()
        self.disconnect()

        return paste
      
    def editPaste(self, paste_id, group_id, parent_id, category_id, user_id, paste_content):
        """
            editPaste
            function to edit a paste
            @param paste_id Id of the paste
            @param group_id Group Id for the new paste
            @param parent_id Id of this pastes parent
            @param category_id Category Id for this paste
            @param user_id Id of the editing user
            @param paste_content Content of the paste
            @access public
        """
        
        if not paste_id:
            raise DbPasteError("No paste ID submitted")
        
        self.getConnection()
        cursor  = self.connection.cursor()

        cursor.execute('''UPDATE pb_pastes
                            SET group_id=%i,
                                user_id=%i,
                                parent_id=%i,
                                category_id=%i
                            WHERE id=%i''',(group_id, user_id, parent_id, category_id, paste_id))
        paste_id = self.connection.insert_id()
        self.getConnection().commit()
        cursor.execute('''UPDATE pb_pastescontent
                            SET datum=date(),
                                content=%s
                            WHERE paste_id=%i''',(paste_content, paste_id))
        self.getConnection().commit()
        self.disconnect()
