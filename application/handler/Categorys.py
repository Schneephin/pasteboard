from application.db.Categorys import Category as dbCategory


class Category:
    """
        Category: 
        Category-handler class handles all requests for category
        this class know witch db - handler class to use to
        get or set data to db
        
        @package application/handler
        @version $id$
        @author Anja Siek <anja.marita@web.de> 
    """
    def __init__(self):
        """
            __init__ 
            creates class-vars dbCategory and categorys 

            @author Anja Siek <anja.marita@web.de> 
            @access private
        """
        self.dbCategory = dbCategory()
        self.categorys = []

    def createCategory(self, categorystring):
        """
            createCategory 
            handels categorystring so that db-object can write it
            
            @author Anja Siek <anja.marita@web.de> 
            @param categorystring categorystring 
            @access public
        """
        categorys = categorystring.split("/");
        catid = 0

        for cat in categorys:
            catid = self.dbCategory.createCategory(cat, catid)

    def getAllCategorys(self):
        """
            getAllCategorys 
            get all categorys from db and return it
            format return so that its orderd by parent ids
            
            @author Anja Siek <anja.marita@web.de> 
            @access public
        """
        categorys = self.dbCategory.getAllCategorys()
        result = {}

        for value in categorys:
            if not value['parent_id'] in result:
                result[value['parent_id']] = {};

            result[value['parent_id']][value['id']] = value['name']
        
        return result

    def saveCategorys(self, categorystring):
        """
            saveCategorys 
            get categorystring split it and use dbobject to write 
            all not existing categorys
            
            @author Anja Siek <anja.marita@web.de> 
            @param categorystring categorystring 
            @access public
        """

        categorys = categorystring.split("/");
        parent = 0;
        
        for category in categorys:
            cat = self.dbCategory.findCategoryByName(category)
            if cat:
                parent = cat['id']
            else:
                self.dbCategory.createCategory(category,parent)
                cat = self.dbCategory.findCategoryByName(category)
                parent = cat['id']

    def findAllCategorys(self,categoryid):
        """
            findAllCategorys 
            find category and all its sub-categorys and return it

            @param categoryid categoryid 
            @access public
        """
        
        cat = self.dbCategory.findCategoryById(categoryid)
        if cat :
            self.categorys.append(cat['id'])
        if cat or categoryid == 0:  
            cats =  self.dbCategory.findAllCategorysByParent(categoryid)
            for category in cats:
                self.findAllCategorys(category['id'])

        return self.categorys
