from application.db.connect import DB
import hashlib,time

class DbTokenError(Exception):
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

class Token(DB):

    def __init__(self):
        # call parant init-method
        super().__init__()

    def generate_hash(self):
        """
            generate_hash 
            function to generate hash-key 
            @access public
        """
        return hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()

    def createToken(self, userId):

        token = self.generate_hash()
        self.getConnection()
        cursor  = self.connection.cursor()

        cursor.execute('REPLACE INTO pb_token (user_id,token)  VALUES (%s,%s)',(userId,token))
        self.getConnection().commit()
        self.disconnect()
        return token
    
    def getUserIdbyToken(self, token):
        self.getConnection()
        cursor = self.connection.cursor()
        cursor.execute('SELECT user_id FROM pb_token WHERE token = %s ',(token))
        uid = cursor.fetchone()
        if not uid or  not uid[0] > 0:
            #error token not exists
            raise DbTokenError("token is not valid") 
        self.getConnection().commit()
        self.disconnect()
        return uid[0]
 
