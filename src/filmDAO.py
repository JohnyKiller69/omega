from dbConn import databaseConnector


class film:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()

    def nejsledovanejsi(self):
        """
        Metoda slouží k vybrání všech rezervací z databáze.
        :return: None.
        """
        self.database_connection.cursor.execute("select * from rezervace;")
    def get_film_by_id(self,film_id):
        """
        Metoda získá název filmu pro danné promítání.
        :param film_id: Id promítání.
        :return: Název filmu.
        """
        try:
            query = "select film.nazev_filmu " \
                    "FROM promitani " \
                    "JOIN film ON promitani.film_id = film.id " \
                    "WHERE promitani.id = %s"
            value = (film_id,)
            self.database_connection.cursor.execute(query,value)
        except:
            raise Exception("Neco se nepovedlo")
        return self.database_connection.cursor.fetchall()

    def insert_film(self,zanr,nazev,delka,rok):
        """
        Metoda slouží pro vložení nového filmu do databáze.
        :param zanr: Id žánru.
        :param nazev: Název filmu.
        :param delka: Délka filmu.
        :param rok: Rok vydání filmu.
        :return: None.
        """
        try:
            query = ("INSERT into film(zanr_id,nazev_filmu,delka,rok_vydani) values(%s,%s,%s,%s)")
            values = (zanr,nazev,delka,rok,)
            self.database_connection.cursor.execute(query, values)
            self.database_connection.connection.commit()
        except Exception as e:
            print(e)

    def get_all(self):
        """
        Metoda slouží k získání všech filmů z databáze.
        :return: None.
        """
        query = "select id,nazev_filmu,delka,rok_vydani from film"
        self.database_connection.cursor.execute(query)
        filmy = self.database_connection.cursor.fetchall()
        return filmy









