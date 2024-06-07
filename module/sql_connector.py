import mysql.connector
from mysql.connector import Error

# Funktion zur Erstellung einer Verbindung zur MySQL-Datenbank
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            database="praktikumsplattform"
        )
        print("Verbindung zur MySQL-Datenbank erfolgreich")
    except Error as e:
        print(f"Fehler bei der Verbindung zur MySQL-Datenbank: {e}")
    return connection