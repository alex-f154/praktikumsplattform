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

# Funktion zur Erstellung der Tabellen
def create_tables(conn):
    sql_create_schueler_table = """CREATE TABLE IF NOT EXISTS schueler (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    username_schueler VARCHAR(255) NOT NULL UNIQUE,
                                    password_schueler VARCHAR(255) NOT NULL,
                                    wunschberuf VARCHAR(255),
                                    strasse VARCHAR(255),
                                    ort VARCHAR(255)
                                );"""
    
    sql_create_betriebe_table = """CREATE TABLE IF NOT EXISTS betriebe (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    username_betrieb VARCHAR(255) NOT NULL UNIQUE,
                                    password_betrieb VARCHAR(255) NOT NULL,
                                    strasse VARCHAR(255),
                                    ort VARCHAR(255)
                                );"""
    
    cursor = conn.cursor()
    cursor.execute(sql_create_schueler_table)
    cursor.execute(sql_create_betriebe_table)
    conn.commit()

# Funktion zur Registrierung eines neuen Schülers
def register_schueler(conn):
    zustimmung = input("Stimmen Sie der Speicherung personenbezogener Daten zu? Ja(1), Nein(2) ")

    if zustimmung == "1":
        print("Speicherung Personenbezogener Daten zugestimmt.")
        username = input("Geben Sie den Benutzernamen ein: ")
        while True:
            password = input("Geben Sie das Passwort ein: ")
            password_confirm = input("Geben Sie das Passwort erneut ein: ")
            if password == password_confirm:
                break
            else:
                print("Passwörter stimmen nicht überein. Bitte erneut eingeben.")
        wunschberuf = input("Geben Sie den Wunschberuf ein: ")
        strasse = input("Geben Sie die Straße ein: ")
        ort = input("Geben Sie den Ort ein: ")

        sql = '''INSERT INTO schueler (username_schueler, password_schueler, wunschberuf, strasse, ort) 
             VALUES (%s, %s, %s, %s, %s)'''
        cursor = conn.cursor()
        cursor.execute(sql, (username, password, wunschberuf, strasse, ort))
        conn.commit()
        print("Schüler erfolgreich registriert")

    elif zustimmung == "2":
        print("Registrierung abgebrochen")
        return
    
    else:
        print("Ungültige Eingabe. Registrierung abgebrochen.")

# Funktion zur Registrierung eines neuen Betriebs
def register_betrieb(conn):
    username = input("Geben Sie den Benutzernamen ein: ")
    while True:
            password = input("Geben Sie das Passwort ein: ")
            password_confirm = input("Geben Sie das Passwort erneut ein: ")
            if password == password_confirm:
                break
            else:
                print("Passwörter stimmen nicht überein. Bitte erneut eingeben.")
    strasse = input("Geben Sie die Straße ein: ")
    ort = input("Geben Sie den Ort ein: ")

    sql = '''INSERT INTO betriebe (username_betrieb, password_betrieb, strasse, ort) 
             VALUES (%s, %s, %s, %s)'''
    cursor = conn.cursor()
    cursor.execute(sql, (username, password, strasse, ort))
    conn.commit()
    print("Betrieb erfolgreich registriert")

# Funktion für den Login
def login(conn, table, username_column, password_column):
    username = input("Geben Sie den Benutzernamen ein: ")
    password = input("Geben Sie das Passwort ein: ")
    
    sql = f"SELECT * FROM {table} WHERE {username_column} = %s AND {password_column} = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    
    if result:
        print("Login erfolgreich")
    else:
        print("Benutzername oder Passwort falsch")

# Hauptfunktion zum Ausführen des Programms
def main():
    database = "praktikumsplattform"
    conn = create_connection("localhost", "dein_benutzername", "dein_passwort", database)

    if conn is not None:
        # Tabellen erstellen
        create_tables(conn)

        # Benutzerentscheidung für Login oder Registrierung
        print("Möchten Sie sich Anmelden(1), Registrieren(2) oder Abbrechen(3)? ")
        auswahl_typ = input("Bitte wählen Sie (1), (2) oder (3): ")

        if auswahl_typ == '1':
            print("Login:")
            auswahl_art = input("Sind Sie ein Schüler(1) oder ein Betrieb(2)? ")
            if auswahl_art == '1':
                login(conn, 'schueler', 'username_schueler', 'password_schueler')
            elif auswahl_art == '2':
                login(conn, 'betriebe', 'username_betrieb', 'password_betrieb')
            else:
                print("Ungültige Auswahl")
        elif auswahl_typ == '2':
            print("Registrierung:")
            auswahl_art = input("Möchten Sie sich als Schüler(1) oder als Betrieb(2) registrieren? ")
            if auswahl_art == '1':
                register_schueler(conn)
            elif auswahl_art == '2':
                register_betrieb(conn)
            else:
                print("Ungültige Auswahl")
        elif auswahl_typ == '3':
            print("Abbruch")
            return
        else:
            print("Ungültige Auswahl")

        conn.close()
    else:
        print("Fehler! Keine Verbindung zur Datenbank.")

if __name__ == '__main__':
    main()
