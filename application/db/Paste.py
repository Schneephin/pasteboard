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
        container class for pastes and uses the pb_pastes and pb_pastescontent tables
        provides a number of functions for pastes like create, edit and get and takes care of the underlying sql
        @package application
        @author Christian Wenzlick <christian.wenzlick@siemens.com> 
        @version $id$
    """
    def __init__(self):
        # call parent init-method
        super().__init__()
        
    def createNewPaste(self, parent_id, category_id, user_id, paste_content, title):
        """
            createNewPaste 
            function to create a new paste
            @param parent_id Id of this pastes parent
            @param category_id Category Id for this paste
            @param user_id Id of the creating user
            @param paste_content Content of the paste
            @param title The title of the paste
            @author Christian Wenzlick <christian.wenzlick@siemens.com> 
            @access public
        """
        
        # user_id, paste_content and title are required fields, all the others are optional
        if not user_id:
            raise DbPasteError("No user ID submitted")
        if not paste_content:
            raise DbPasteError("No content submitted")
        if not title:
            raise DbPasteError("No title submitted")

        self.getConnection()
        cursor  = self.connection.cursor()
                
        cursor.execute('INSERT INTO pb_pastes (parent_id, category_id, user_id)  VALUES (%s, %s, %s)',(parent_id, category_id, user_id))
        # the id is auto-incremented, so we need to get the actual value here
        paste_id = self.connection.insert_id()
        self.getConnection().commit()
        cursor.execute('INSERT INTO pb_pastescontent (paste_id, content, title)  VALUES (%s, %s, %s)',(paste_id, paste_content, title))
        self.getConnection().commit()
        self.disconnect()
        
        return paste_id

    def getAllPastesByUser(self, user_id):
        """
            getAllPastesByUser 
            function to get all pastes created by a specific user
            @param user_id Id of the user
            @author Christian Wenzlick <christian.wenzlick@siemens.com> 
            @access public
        """
        
        if not user_id:
            raise DbPasteError("No user ID submitted")
            
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute('''SELECT 
                        pb_pastes.id as paste_id,
                        pb_pastes.parent_id as parent_id,
                        pb_pastes.category_id as category_id,
                        pb_pastes.user_id as user_id,
                        pb_pastescontent.content as paste_content,
                        pb_pastescontent.datum as datum,
                        pb_pastescontent.title as title
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
            @author Christian Wenzlick <christian.wenzlick@siemens.com> 
            @access public
        """
        if not paste_id:
            raise DbPasteError("No paste ID submitted")
        
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute('''    SELECT 
                            pb_pastes.id as paste_id,
                            pb_pastes.parent_id as parent_id,
                            pb_pastes.category_id as category_id,
                            pb_pastes.user_id as user_id,
                            pb_pastescontent.content as paste_content,
                            pb_pastescontetn.datum as datum,
                            pb_pastescontent.title as title
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
            @author Christian Wenzlick <christian.wenzlick@siemens.com> 
            @access public
        """
        if not category_id:
            raise DbPasteError("No category ID submitted")
        
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute('''  SELECT 
                            pb_pastes.id as paste_id,
                            pb_pastes.parent_id as parent_id,
                            pb_pastes.category_id as category_id,
                            pb_pastes.user_id as user_id,
                            pb_pastescontent.content as paste_content,
                            pb_pastescontent.datum as datum,
                            pb_pastescontent.title as title
                        FROM pb_pastes JOIN pb_pastescontent ON pb_pastes.id = pb_pastescontent.paste_id 
                        WHERE pb_pastes.category_id = %s''',(category_id))
        pastes = cursor.fetchall()
        cursor.close() 
        return pastes
    
    def getPasteByID (self, paste_id):
        """
            getPasteByID 
            function to get a paste by id
            @param paste_id id of the paste
            @author Christian Wenzlick <christian.wenzlick@siemens.com> 
            @access public
        """
        if not paste_id:
            raise DbPasteError("No paste ID submitted")

        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute(''' SELECT 
                           pb_pastes.id as paste_id,
                           pb_pastes.parent_id as parent_id,
                           pb_pastes.category_id as category_id,
                           pb_categorys.name as category_name,
                           pb_pastes.user_id as paste_user_id,
                           pb_pastescontent.content as paste_content,
                           pb_pastescontent.datum as datum,
                           pb_pastescontent.title as title
                       FROM pb_pastes JOIN pb_pastescontent ON pb_pastes.id = pb_pastescontent.paste_id JOIN pb_categorys ON pb_pastes.category_id = pb_categorys.id
                       WHERE pb_pastes.id = %s''',(paste_id))
        paste = cursor.fetchone()
        cursor.close()       
        if not paste:
            raise DbPasteError("No paste found for this ID")

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
            @author Christian Wenzlick <christian.wenzlick@siemens.com> 
            @access public
        """
        
        if not paste_id:
            raise DbPasteError("No paste ID submitted")
        
        self.getConnection()
        cursor  = self.connection.cursor()

        cursor.execute('''UPDATE pb_pastes
                            SET user_id=%i,
                                parent_id=%i,
                                category_id=%i
                            WHERE id=%i''',(user_id, parent_id, category_id, paste_id))
        self.getConnection().commit()
        cursor.execute('''UPDATE pb_pastescontent
                            SET datum=date(),
                                content=%s,
                                title=%s
                            WHERE paste_id=%i''',(paste_content, title, paste_id))
        self.getConnection().commit()
        self.disconnect()
