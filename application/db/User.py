from application.db.connect import DB
import hashlib

class DbUserError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class User(DB):
    def __init__(self):
        super().__init__()

    def createUser(self,key):
        self.getConnection()
        cursor  = self.connection.cursor()

        cursor.execute('INSERT INTO pb_users (invitekey)  VALUES (%s)',(key))
        self.getConnection().commit()
        self.disconnect()

    def register (self, uname, email, passw, ikey):
        self.getConnection()
        cursor  = self.connection.cursor()

        cursor.execute('SELECT id, email FROM pb_users WHERE invitekey = %s',(ikey))
        uid = cursor.fetchone()
        if not uid or  not uid[0] > 0:
            raise DbUserError("invite Key is not valid")
        if uid[1]:
            raise DbUserError("this invitekey has already been used")
        
        password = self.getMd5(passw)
        cursor.execute('UPDATE pb_users SET email = %s WHERE invitekey = %s',(email, ikey))
        cursor.execute('INSERT INTO pb_userdata (userId,username,password) VALUES (%s, %s,%s)',(uid[0],uname,password))
        self.getConnection().commit()
        self.disconnect()

    def getMd5(self,passw):
        password = hashlib.md5(passw.encode('utf-8')).hexdigest()
        return password

    def login(self, email,passw):
        password = self.getMd5(passw)
        
        self.getConnection()
        cursor  = self.connection.cursor()
        cursor.execute('SELECT id FROM pb_users WHERE email = %s',(email))
        uid = cursor.fetchone()
        if not uid or  not uid[0] > 0:
            raise DbUserError("email or password wrong")

        cursor.execute('SELECT password FROM pb_userdata WHERE userId = %s',uid[0])
        pw = cursor.fetchone()
        if not pw[0] == password:
            raise DbUserError("email or password wrong")

        return True 




