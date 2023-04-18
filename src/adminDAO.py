from dbConn import databaseConnector
class Admin:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()

    def get_role(self,id):
        """
        Metoda slouží pro získání role uživatele podle jeho id.
        :param id: Id uživatele.
        :return: Role uživatele.
        """
        query = "SELECT  role FROM admin" \
                " where id = %s"
        value = (id,)
        self.database_connection.cursor.execute(query, value)
        role = self.database_connection.cursor.fetchone()
        return role

    def get_pohlavi(self,jmeno):
        """
        Metoda slouží pro získání pohlaví uživatele z databáze.
        :param jmeno: Jmébo uživatele.
        :return: Pohlaví uživatele.
        """
        query = "SELECT  sex FROM admin" \
                " where id = %s"
        value = (jmeno,)
        self.database_connection.cursor.execute(query, value)
        pohlavi = self.database_connection.cursor.fetchone()
        return pohlavi
    def update_jmena(self,stare_jm,nove_jm):
        """
        Metoda slouží k updatnutí jména v databázi podle starého jména.
        :param stare_jm: Staré jméno uživatele.
        :param nove_jm: Nové jméno uživatele.
        :return: None
        """
        try:
            query = "update admin " \
                    "set username = %s " \
                    "where username = %s"
            values = (nove_jm,stare_jm,)
            self.database_connection.cursor.execute(query, values)
            self.database_connection.connection.commit()
        except:
            self.database_connection.connection.rollback()

    def kontrola_jmena(self,jmeno):
        """
        Metoda slouží ke kontrole zdali s tímto jménem již někdo neexistuje.
        :param jmeno: Jméno uživatele.
        :return: None
        """
        query = "SELECT COUNT(*) FROM admin " \
                "WHERE username = %s "
        param = (jmeno,)
        self.database_connection.cursor.execute(query, param)
        result = self.database_connection.cursor.fetchone()
        if result[0] > 0:
            raise Exception("Uživatel již existuje")

    def get_id(self,jmeno):
        """
        Metoda slouží k získání id uživatele podle jeho jména.
        :param jmeno: Jméno uživatele.
        :return: Id uživatele.
        """
        query = "SELECT  id FROM admin" \
                " where username = %s"
        value = (jmeno,)
        self.database_connection.cursor.execute(query, value)
        id = self.database_connection.cursor.fetchone()
        return id

    def get_jmeno(self,id):
        """
        Metoda slouží k získá jména uživatele podle id.
        :param id: Id uživatele.
        :return: Jméno uživatele.
        """
        query = "SELECT  username FROM admin" \
                " where id = %s"
        value = (id,)
        self.database_connection.cursor.execute(query, value)
        jmeno = self.database_connection.cursor.fetchone()
        return jmeno

    def get_heslo(self,jmeno,heslo):
        """
        Metoda slouží k ověření zdali původní heslo bylo zadáno správně.
        :param jmeno: Jméno uživatele.
        :param heslo: Heslo uživatele.
        :return: None
        """
        query = "SELECT  password FROM admin" \
                " where username = %s"
        value = (jmeno,)
        self.database_connection.cursor.execute(query, value)
        check_heslo = self.database_connection.cursor.fetchone()
        if check_heslo[0] != heslo:
            raise Exception("Původní heslo není správné!")
        return

    def update_heslo(self,jmeno,heslo):
        """
        Metoda slouží k updatnutí hesla v databázi.
        :param jmeno: Jméno uživatele.
        :param heslo: Nové heslo uživatele.
        :return: None
        """
        try:
            query = "update admin " \
                    "set password = %s " \
                    "where username = %s"
            values = (heslo,jmeno,)
            self.database_connection.cursor.execute(query, values)
            self.database_connection.connection.commit()
            return True
        except:
            self.database_connection.connection.rollback()

    def get_all(self):
        """
        Metoda slouží pro získání všech zaměstnanců.
        :return: Pole zaměstnanců.
        """
        try:
            query = "select id, username, sex, role from admin"
            self.database_connection.cursor.execute(query)
            pracovnici = self.database_connection.cursor.fetchall()
            return pracovnici
        except:
            raise Exception("Něco se nepovedlo!")

    def delete_pracovnik(self,id):
        """
        Metoda slouží k odstranění zaměstnance z databáze.
        :param id: Id pracovníka.
        :return: None
        """
        query = "delete from admin " \
                "where id = %s"
        value = (id,)
        self.database_connection.cursor.execute(query,value)
        self.database_connection.connection.commit()







