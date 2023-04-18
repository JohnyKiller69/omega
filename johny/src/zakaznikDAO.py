from dbConn import databaseConnector

class zakaznik:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()

    def email_exists(self,email):
        query = "SELECT COUNT(*) FROM zakaznik " \
                "WHERE email = %s"
        value = (email,)
        self.database_connection.cursor.execute(query, value)
        pocet = self.database_connection.cursor.fetchone()
        if pocet[0] == 1:
            return
        else:
            raise Exception("Zadali jste neplatný email.")

    def prevod_kreditu(self, jmeno, prijmeni, emailAdresata, kredity):
        """

        :param jmeno: jméno zákazníka
        :param prijmeni: příjmení zákazníka
        :param emailAdresata: email zákazníka, kterému se pošlou kredity
        :param kredity: kredity, které posíláme
        :return: None

        Metoda služí pro převod kreditů mezi uživateli.
        """
        kredity = int(kredity)
        if kredity < 0:
            raise Exception("Špatná hodnota!")
        else:
            query = "select zakaznik.body " \
                    "from zakaznik " \
                    "where jmeno = %s and prijmeni = %s"
            values = (jmeno,prijmeni,)
            self.database_connection.cursor.execute(query,values)
            kredit = self.database_connection.cursor.fetchone()
            kredit = int(kredit[0])
            if kredit < kredity:
                raise Exception ("Nemáte dostatek kreditů!")
            else:
                self.database_connection.cursor.execute("START TRANSACTION")
                query = "select zakaznik.id from zakaznik where email = %s "
                values = (emailAdresata,)
                self.database_connection.cursor.execute(query, values)
                email = self.database_connection.cursor.fetchone()
                if email != None:
                    query = "update zakaznik " \
                            "set body = body-%s " \
                            "where jmeno = %s and prijmeni = %s "
                    values = (kredity, jmeno, prijmeni,)
                    self.database_connection.cursor.execute(query, values)
                    query = "update zakaznik " \
                            "set body =body+ %s " \
                            "where email = %s "
                    value = (kredity, emailAdresata,)
                    self.database_connection.cursor.execute(query, value)
                    self.database_connection.connection.commit()
                    zustatek = kredit - kredity
                    
                else:
                    raise Exception ("Neznámý email!")
        return (f"Zbylo vám {zustatek}kreditů")

    def uzv_exists_jm(self,jmeno,prijmeni):
        query = "SELECT COUNT(*) FROM zakaznik " \
                "WHERE jmeno = %s and prijmeni = %s"
        value = (jmeno, prijmeni,)
        self.database_connection.cursor.execute(query, value)
        pocet = self.database_connection.cursor.fetchone()
        if pocet[0] == 1:
            return
        else:
            raise Exception("Uživatel neexistuje")
    def uzv_exists(self,email):
        query = "SELECT COUNT(*) FROM zakaznik " \
                "WHERE email = %s"
        value = (email,)
        self.database_connection.cursor.execute(query, value)
        pocet = self.database_connection.cursor.fetchone()
        if pocet[0] > 0:
            raise Exception("Email již existuje")
        else:
            return

    def uzv_exists_jm_pr(self, jmeno,prijmeni,email,telefon,vek):
        query = "SELECT COUNT(*) FROM zakaznik " \
                "WHERE jmeno = %s and prijmeni = %s"
        value = (jmeno,prijmeni,)
        self.database_connection.cursor.execute(query, value)
        pocet = self.database_connection.cursor.fetchone()
        if pocet[0] > 0:
            raise Exception("Uživatel již existuje")
        else:

            try:
                query = "INSERT into zakaznik(jmeno,prijmeni,email,telefon,vek) values(%s,%s,%s,%s,%s)"
                params = (jmeno,prijmeni,email,telefon,vek,)
                self.database_connection.cursor.execute(query, params)
                self.database_connection.connection.commit()
                return True
            except:
                raise Exception("Neco se nepovedlo")

    def get_uzivatel(self):
        query = "select * from zakaznik"
        self.database_connection.cursor.execute(query)
        zakaznici = self.database_connection.cursor.fetchall()
        return zakaznici

    def update_tel(self, id, telefon):
        query = "SELECT COUNT(*) FROM zakaznik " \
                "WHERE telefon = %s "
        param = (telefon,)
        self.database_connection.cursor.execute(query, param)
        result = self.database_connection.cursor.fetchone()
        if result[0] > 0:
            raise Exception("Telefoní číslo již existuje.")
        else:
            query = "update zakaznik " \
                    "set telefon = %s " \
                    "where id = %s"
            params = (telefon,id,)
            self.database_connection.cursor.execute(query, params)
            self.database_connection.connection.commit()

    def update_email(self, id , email):
        query = "SELECT COUNT(*) FROM zakaznik " \
                "WHERE email = %s"
        param = (email,)
        self.database_connection.cursor.execute(query, param)
        result = self.database_connection.cursor.fetchone()
        if result[0] > 0:
            return False
        try:
            query = "update zakaznik " \
                    "set email = %s " \
                    "where id = %s"
            params = (email, id,)
            self.database_connection.cursor.execute(query, params)
            self.database_connection.connection.commit()
        except:
            raise Exception("Neco se nepovedlo")

    def remove_zak(self,id):
        try:
            query = "delete from zakaznik " \
                    "where id = %s"
            value = (id,)
            self.database_connection.cursor.execute(query, value)
            self.database_connection.connection.commit()
        except:
            raise Exception("Neco se nepovedlo")










