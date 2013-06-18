from application.db.Categorys import Category as dbCategory


class Category:

    def __init__(self):
        self.dbCategory = dbCategory()
        self.categorys = []

    def createCategory(self, categorystring):
        categorys = categorystring.split("/");
        catid = 0

        for cat in categorys:
            catid = self.dbCategory.createCategory(cat, catid)

    def getAllCategorys(self):
        categorys = self.dbCategory.getAllCategorys()
        result = {}

        for value in categorys:
            if not value['parent_id'] in result:
                result[value['parent_id']] = {};

            result[value['parent_id']][value['id']] = value['name']
        
        return result

    def saveCategorys(self, categorystring):

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
        
        cat = self.dbCategory.findCategoryById(categoryid)
        if cat :
            self.categorys.append(cat['id'])
        if cat or categoryid == 0:  
            cats =  self.dbCategory.findAllCategorysByParent(categoryid)
            for category in cats:
                self.findAllCategorys(category['id'])

        return self.categorys
