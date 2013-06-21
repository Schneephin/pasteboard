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
        class to handle pb_categorys table on db 
        extends connect.DB class so that all functions from 
        connect.DB are availeble
        
        @version $id$
        @package application/db
        @author Anja Siek <anja.marita@web.de>
    """
    def __init__(self):
        # call parant init-method
        super().__init__()

    def createCategory(self, category, parentId):
        """
            createCategory 
            insert category into db
            
            @author Anja Siek <anja.marita@web.de>
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
            return all categorys
            
            @author Anja Siek <anja.marita@web.de>
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
        """
            findCategoryByName 
            find category by name
            
            @author Anja Siek <anja.marita@web.de>
            @param name name 
            @access public
        """
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pb_categorys WHERE name = %s', (name))
        category = cursor.fetchone()
        self.getConnection().commit() 

        return category

    def findCategoryById(self,catid):
        """
            findCategoryById 
            find category by id
            
            @author Anja Siek <anja.marita@web.de>
            @param catid catid 
            @access public
        """
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pb_categorys WHERE id = %s', (catid))
        category = cursor.fetchone()
        cursor.close()

        return category

    def findAllCategorysByParent(self,parentId):
        """
            findAllCategorysByParent 
            get all subcategorys by its parentid
            
            @author Anja Siek <anja.marita@web.de>
            @param parentId parentId 
            @access public
        """
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor)
        cursor.execute("SELECT id FROM pb_categorys WHERE parent_id = %s", (parentId)) 
        categorys = cursor.fetchall()
        cursor.close()
        return categorys
