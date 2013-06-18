from application.db.connect import DB

class DbCategoryError(Exception):
    """
        DbCategoryError(Exception): 
        Exception for Category-Db Class
        
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

class Category(DB):

    """
        Category(DB): 
        
        @package 
        @version $id$
        @copyright 
        @author Anja Siek <ja.sie.kan@gmail.com> 
        @license 
    """
    def __init__(self):
        # call parant init-method
        super().__init__()

    def createCategory(self, category, parentId):
        """
            createCategory 
            
            @param category category 
            @param parentId parentId 
            @access public
        """

        self.getConnection()
        cursor  = self.connection.cursor(self.mdb.cursors.DictCursor)

        result = cursor.execute('INSERT IGNORE INTO pb_categorys (name, parent_id)  VALUES (%s,%s)',(category,parentId))
        self.getConnection().commit()
        return result

    def getAllCategorys(self):
        """
            getAllCategorys 
            
            @access public
        """
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor)

        cursor.execute('SELECT * FROM pb_categorys')
        categorys = cursor.fetchall()
        self.getConnection().commit() 
        self.disconnect()

        return categorys

    def findCategoryByName(self,name):
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pb_categorys WHERE name = %s', (name))
        category = cursor.fetchone()
        self.getConnection().commit() 

        return category

    def findCategoryById(self,catid):
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pb_categorys WHERE id = %s', (catid))
        category = cursor.fetchone()
        cursor.close()

        return category

    def findAllCategorysByParent(self,parentId):
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor)
        cursor.execute("SELECT id FROM pb_categorys WHERE parent_id = %s", (parentId)) 
        categorys = cursor.fetchall()
        cursor.close()
        return categorys
