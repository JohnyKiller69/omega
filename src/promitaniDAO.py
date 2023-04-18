from dbConn import databaseConnector
class promitani:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()

    def all_rezervace(self):
        try:
            query = "select * from promitani "
            self.database_connection.cursor.execute(query)
            return self.database_connection.cursor.fetchall()
        except:
            raise Exception("neco se nepovedlo")

    def cas_promitani(self,id):
        try:
            query = "select * from promitani " \
                    "where id= %s"
            value = (id,)
            self.database_connection.cursor.execute(query,value)
            return self.database_connection.cursor.fetchall()
        except:
            raise Exception("neco se nepovedlo")

    def insert(self,film_id,sal_id,datum,cas,cena):
        query = ("INSERT into promitani(film_id,sal_id,datum,cas,cena) values(%s,%s,%s,%s,%s)")
        values = (film_id,sal_id,datum,cas,cena,)
        self.database_connection.cursor.execute(query, values)
        self.database_connection.connection.commit()



