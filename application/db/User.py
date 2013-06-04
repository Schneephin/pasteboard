from application.db.connect import DB
import hashlib

class DbUserError(Exception):
    """
        DbUserError(Exception): 
        Exception for User-Db Class
        
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

class User(DB):
    """
        User(DB): 
        extends connect.DB class so that all functions from 
        connect.DB are availeble
        @package application
        @author Anja Siek <anja.marita@web.de>
        @version $id$
    """
    def __init__(self):
        # call parant init-method
        super().__init__()

    def createUser(self,key):
        """
            createUser 
            function to create a new user with its invitekey
            @param key key 
            @access public
        """
        self.getConnection()
        cursor  = self.connection.cursor()

        cursor.execute('INSERT INTO pb_users (invitekey)  VALUES (%s)',(key))
        self.getConnection().commit()
        self.disconnect()

    def register (self, uname, email, passw, ikey):
        """
            register 
            function for registration with correct invitekey 
            @param uname uname 
            @param email email 
            @param passw passw 
            @param ikey ikey 
            @access public
        """
        self.getConnection()
        cursor  = self.connection.cursor()

        #first check for entry with invitekey exists
        cursor.execute('SELECT id, email FROM pb_users WHERE invitekey = %s',(ikey))
        uid = cursor.fetchone()
        if not uid or  not uid[0] > 0:
            #error invitekey not exists
            raise DbUserError("invite Key is not valid")
        if uid[1]:
            #error user is already registerd
            raise DbUserError("this invitekey has already been used")

        #if all is ok save data to user
        password = self.getMd5(passw)
        cursor.execute('UPDATE pb_users SET email = %s,password = %s WHERE invitekey = %s',(email,password, ikey))
        cursor.execute('INSERT INTO pb_userdata (user_id,username) VALUES (%s, %s)',(uid[0],uname))
        self.getConnection().commit()
        self.disconnect()
        return uid[0]

    def getMd5(self,passw):
        """
            getMd5 
            generates an md5 for password
            @param passw passw 
            @access public
        """
        password = hashlib.md5(passw.encode('utf-8')).hexdigest()
        return password

    def login(self, email, passw):
        """
            login 
            login function check password and email
            @param email email 
            @param passw passw 
            @access public
        """

        password = self.getMd5(passw)
        
        self.getConnection()
        cursor  = self.connection.cursor()
        cursor.execute('SELECT id,password FROM pb_users WHERE email = %s',(email))
        user = cursor.fetchone()
        if not user or not user[0] > 0 or not user[1] or not user[1] == password:
            #error no user for email found
            raise DbUserError("email or password wrong")

        return user[0] 

    def getUserData(self, uid):
        self.getConnection()
        cursor = self.connection.cursor(self.mdb.cursors.DictCursor) 
        cursor.execute(
                """SELECT 
                    a.user_id as id, 
                    a.username as username, 
                    b.email as email  
                FROM 
                    pb_userdata as a 
                JOIN 
                    pb_users as b
                ON  
                    a.user_id = b.id 
                WHERE 
                    a.user_id = %s""",uid)
        user = cursor.fetchone()
        self.getConnection().commit()
        self.disconnect()

        return user




