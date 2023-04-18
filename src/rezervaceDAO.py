import datetime
from dbConn import databaseConnector

class rezervace:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()

    def vytvoreni_rezervace(self, promitani, jmeno,prijmeni, osobne):
        """
        :param promitani: id promitání
        :param jmeno: jméno  zákazníka
        :param prijmeni: příjmení zákazníka
        :param osobne: osobně nebo online
        :return: None

        Metoda slouží k vytvoření rezervace v databázi.
        """
        query = "select zakaznik.id " \
                "from zakaznik " \
                "where jmeno = %s and prijmeni = %s"
        values = (jmeno, prijmeni,)
        self.database_connection.cursor.execute(query, values)
        id = self.database_connection.cursor.fetchone()
        if id != None:
            id = int(id[0])
            now = datetime.datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            query = "insert into rezervace(promitani_id, zakaznik_id, osobne,cas_rezervace) values (%s, %s, %s,%s)"
            values = (promitani, id, osobne,formatted_date,)
            self.database_connection.cursor.execute(query, values)
            query = "update zakaznik " \
                    "set body=body+20 " \
                    "where zakaznik.id= (%s)"
            values = (id,)
            self.database_connection.cursor.execute(query, values)
            self.database_connection.connection.commit()
        else:
            raise Exception ("Špatné jméno nebo příjmení")
    def get_rezervace(self):
        query = "select * from rezervace "
        self.database_connection.cursor.execute(query)
        return self.database_connection.cursor.fetchall()

    def get_rezervace_s_jmeny_prijmenimi(self):
        query = ("""
            SELECT r.id, r.promitani_id, z.jmeno, z.prijmeni, r.osobne, r.cas_rezervace,f.nazev_filmu, p.cas
            FROM rezervace r
            JOIN promitani p ON r.promitani_id = p.id
            JOIN film f ON p.film_id = f.id
            JOIN zakaznik z ON r.zakaznik_id = z.id
        """)
        self.database_connection.cursor.execute(query)
        return self.database_connection.cursor.fetchall()

    def remove_reservation(self, reservation_id):
        query=("DELETE FROM rezervace "
               "WHERE id = %s")
        value = (reservation_id,)
        self.database_connection.cursor.execute(query, value)
        self.database_connection.connection.commit()

    def zruseni_rezervace(self, rezervace, zakaznik):
        """

        :param rezervace: id rezervace
        :param zakaznik: id zakaznika
        :return: None

        Metoda slouží ke zrušení rezervace v databázi.
        """
        try:
            self.database_connection.connection.execute("delete from rezervace "
                                                        "where id = %s and zakaznik_id = %s",(rezervace,zakaznik))
            self.database_connection.connection.execute("update zakaznik "
                                                        "where id = %s set body =body-20",(zakaznik))
            self.database_connection.connection.commit()
        except:
            self.database_connection.connection.rollback()
        finally:
            self.database_connection.connection.close()
    def update_screening_id(self,rezervace,promitani):
        try:
            now = datetime.datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            query = "update  rezervace  " \
                    "set promitani_id = %s,cas_rezervace = %s " \
                    "where id = %s "
            values = (promitani, formatted_date, rezervace)
            self.database_connection.cursor.execute(query,values)
            self.database_connection.connection.commit()
        except:
            self.database_connection.connection.rollback()

    def update_rezervace(self, rezervace, jmeno,prijmeni):
        """

        :param rezervace: id rezervace
        :param jmeno: jméno zákazníka
        :param prijmeni: příjmení zákazníka
        :return: None

        Metode slouží k úpravě rezervace.
        """
        try:
            query = "select zakaznik.id from zakaznik " \
                    "where jmeno = %s and prijmeni = %s"
            values = (jmeno, prijmeni,)
            self.database_connection.cursor.execute(query, values)
            id = self.database_connection.cursor.fetchone()
            if id != None:
                id = int(id[0])
                self.database_connection.connection.execute("update  rezervace  "
                                                            "where id = rezervace "
                                                            "set zakaznik_id = %s",(rezervace,id))
                self.database_connection.connection.commit()
            else:
                raise Exception("Špatné jméno nebo příjmení")
        except:
            self.database_connection.connection.rollback()
        finally:
            self.database_connection.connection.close()








