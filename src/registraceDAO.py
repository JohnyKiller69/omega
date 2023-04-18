import hashlib
from dbConn import databaseConnector

class registraceDB:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()

    def hash_password(self,password):
        """Hashes a password using SHA-256."""
        salt = b'somesalt'
        password = password.encode('utf-8')
        return hashlib.sha256(salt + password).hexdigest()

    def registrace(self,jmeno,heslo,pohlavi,role):
        if pohlavi == 0:
            pohlavi = "muž"
        else:
            pohlavi = "žena"
        heslo = self.hash_password(heslo)
        query = "SELECT COUNT(*) FROM admin " \
                "WHERE username = %s OR password = %s"
        params = (jmeno, heslo)
        self.database_connection.cursor.execute(query, params)
        result = self.database_connection.cursor.fetchone()
        if result[0] > 0:
            raise Exception("Uživatel již existuje")
        try:
            query = "INSERT into admin(username,password,sex,role) values(%s,%s,%s,%s)"
            params = (jmeno, heslo,pohlavi,role)
            self.database_connection.cursor.execute(query, params)
            self.database_connection.connection.commit()
            return True
        except:
            raise Exception("Neco se nepovedlo")


