import csv
from dbConn import databaseConnector
class importy:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()
    def vlozPromitani(self):
        """
        Metoda slouží k vložení dat do databáze z csv souboru.
        :return: None
        """
        cursor = self.database_connection.connection.cursor()
        with open("../data/promitani.csv") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                query = "INSERT INTO promitani ({}) VALUES ({})".format(
                    ", ".join(header),
                    ", ".join(["%s"] * len(row))
                )
                cursor.execute(query, row)
        self.database_connection.connection.commit()

    def vlozZakaznik(self):
        """
        Metoda slouží k vložení dat do databáze z csv souboru.
        :return: None
        """
        cursor = self.database_connection.connection.cursor()
        with open("../data/zakaznik.csv") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                query = "INSERT INTO zakaznik ({}) VALUES ({})".format(
                    ", ".join(header),
                    ", ".join(["%s"] * len(row))
                )
                cursor.execute(query, row)
        self.database_connection.connection.commit()
        self.database_connection.connection.close()


