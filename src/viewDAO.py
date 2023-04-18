from dbConn import databaseConnector
import pandas

class Viewy:
    def __init__(self):
        self.database_connection = databaseConnector.MySQLConnection.getInstance()

    def vydelek(self):
        """

        :return: view

        Metoda slouží k vypsání viewu.
        """
        cursor = self.database_connection.connection.cursor()
        cursor.execute("SELECT * FROM vydelek")
        result = cursor.fetchall()
        cursor.execute("DESCRIBE vydelek")
        column_names = [column[0] for column in cursor.fetchall()]
        cursor.close()

        data = pandas.DataFrame(result, columns=column_names)

        # Add column names as a new row
        column_names_row = pandas.DataFrame([column_names], columns=column_names)
        data = pandas.concat([column_names_row, data], ignore_index=True)

        return data

    def nejsledovanejsi(self):
        """

        :return: view

        Metoda slouží k vypsání viewu.
        """
        cursor = self.database_connection.connection.cursor()
        cursor.execute("SELECT * FROM nejsledovanejsi")
        result = cursor.fetchall()
        cursor.execute("DESCRIBE nejsledovanejsi")
        column_names = [column[0] for column in cursor.fetchall()]
        cursor.close()

        data = pandas.DataFrame(result, columns=column_names)

        # Add column names as a new row
        column_names_row = pandas.DataFrame([column_names], columns=column_names)
        data = pandas.concat([column_names_row, data], ignore_index=True)

        return data


