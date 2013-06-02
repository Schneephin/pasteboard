from application.db.Categorys import Category as dbCategory


class Category:

    def __init__(self):
        self.dbCategory = dbCategory()

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


