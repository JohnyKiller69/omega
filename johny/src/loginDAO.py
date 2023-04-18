from dbConn import databaseConnector
class loginDB:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()

    def prihlaseni(self,jmeno,heslo):
        try:
            query = "SELECT * FROM admin " \
                    "WHERE username = %s AND password = %s"
            params = (jmeno, heslo)
            self.database_connection.cursor.execute(query, params)
            result = self.database_connection.cursor.fetchone()
            return result
        except:
            raise Exception("Neco se nepovedlo")

    def vytvoreniUzivatele(self):
        raise Exception