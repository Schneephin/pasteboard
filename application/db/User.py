from application.db.connect import DB
import oursql as mdb 

class User(DB):
    def __init__(self):
        super().__init__()

    def createUser(self,key):
        self.getConnection()
        cursor  = self.connection.cursor()

        value = mdb.BinaryIterWrapper(['%s' % key])

        cursor.execute('INSERT INTO pb_users (invitekey)  VALUES (?)',(value))
        cursor.commit()
        
        self.disconnect()


