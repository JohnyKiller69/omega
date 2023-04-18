import mysql.connector
import json
import socket

def get_ip():
    """

    :return: ip adresu

    Metoda slouží k získání ip adresy z konfiguračního souboru.
    """
    def is_valid_ip(ip):
        try:
            socket.inet_pton(socket.AF_INET, ip)
            return True
        except socket.error:
            return False

    try:
        conf = open('../databazeFunkcni/data/conf.json', 'r')
        data = conf.read()
        obj = json.loads(data)
        ip = obj["host"]
        conf.close()
        #if is_valid_ip(ip):
        return ip
        #else:
            #raise Exception("Špatný formát ip adresy! Zkontrolujte zda jste ji zadal/a správně.")
    except Exception as e:
        print("Došlo k chybě:", e)

def get_user():
    """

    :return: usera

    Metoda slouži k získání usera z konfiguračního souboru.
    """
    try:
        conf = open('../databazeFunkcni/data/conf.json', 'r')
        data = conf.read()
        obj = json.loads(data)
        user = obj["user"]
        conf.close()
        if user.isalnum():
            return user
        else:
            raise Exception("Nevhodné znaky, nebo špatné jméno.")
    except Exception as e:
        print("Došlo k chybě:", e)

def get_heslo():
    """

    :return: heslo

    Metoda slouži k získání hesla z konfiguračního souboru.
    """
    try:
        conf = open('../databazeFunkcni/data/conf.json', 'r')
        data = conf.read()
        obj = json.loads(data)
        heslo = obj["password"]
        conf.close()
        if heslo.isalnum():
            return heslo
        else:
            raise Exception("Nevhodné znaky, nebo špatné heslo.")
    except Exception as e:
        print("Došlo k chybě:", e)

def get_db():
    """

    :return: název db

    Metoda slouži k získání názvu databáze z konfiguračního souboru.
    """
    try:
        conf = open('../databazeFunkcni/data/conf.json', 'r')
        data = conf.read()
        obj = json.loads(data)
        db = obj["database"]
        conf.close()
        if db.isalnum():
            return db
        else:
            raise Exception("Nevhodné znaky, nebo špatná databáze.")
    except Exception as e:
        print("Došlo k chybě:", e)

class MySQLConnection:
    __instance = None
    connection = None
    cursor = None
    @staticmethod
    def getInstance():
        """

        :return: Instanci třídy MySQLConnection

        Metoda vrací jednu a tuto samou instanci třídy MySQLConnection, pokud již nějaká existuje, jinak ji vytvoří.
        """
        if MySQLConnection.__instance == None:
            MySQLConnection()
        return MySQLConnection.__instance

    def __init__(self):
        if MySQLConnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:

            MySQLConnection.__instance = self
            self.connection = mysql.connector.connect(
              host=get_ip(),
              port=3306,
              user=get_user(),
              password=get_heslo(),
              database=get_db()
            )
            self.cursor = self.connection.cursor()


