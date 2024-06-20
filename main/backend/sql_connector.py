import mysql.connector
from mysql.connector import Error

# Funktion zur Erstellung einer Verbindung zur MySQL-Datenbank
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost", # dieser wert wird in "host_name" eingetragen
            user="root", # dieser wert wird in "user_name" eingetragen
            # wenn man der datenbank ein passwort vergibt, würde man hier password="xxx" eintragen, in unserem falle wird kein passwort für die datenbank erstellt
            database="Praktikumsplattform" # dieser wert wird in "db_name" eingetragen
        )
        print("Verbindung zur MySQL-Datenbank erfolgreich") # bestätigung der erfolgreichen verbindung
    except Error as e:
        print(f"Fehler bei der Verbindung zur MySQL-Datenbank: {e}") # bestätigung der erfolglosen verbindung
    return connection