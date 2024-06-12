# Module importieren, die für die Steuerung mit der Python-Runtime sowie Betriebssystem nötig sind
import sys
import os

# Importieren der benutzerdefinierten Module aus dem 'backend'-Ordner
from backend.sql_connector import create_connection
from backend.registrierung import register_schueler, register_betrieb
from backend.login import login

# Hauptfunktion zum Ausführen des Programms
def main():
    database = "praktikumsplattform"
    conn = create_connection("localhost", "root", "", database)

    if conn is not None:

        # Benutzerentscheidung für Login oder Registrierung | HWK-Admin Anmeldung verborgen
        print("Möchten Sie sich: ")
        print("1) Anmelden" )
        print("2) Registrieren")
        print("3) Abbrechen")
        #print("Anmelden         (1)" )
        #print("Registrieren     (2) ")
        #print("Abbrechen        (3) ")
        print(" ")
        auswahl_typ = input("Auswahl: ")

        if auswahl_typ == '1':
            print(" ")
            print("Login:")
            print(" ")
            auswahl_art = input("Sind Sie ein Schüler(1) oder ein Betrieb(2)? \n \nAuswahl: ")
            if auswahl_art == '1':
                print(" ")
                login(conn, 'Schueler', 'Username_Schueler', 'Passwort_Schueler')
            elif auswahl_art == '2':
                print(" ")
                login(conn, 'betriebe', 'Username_Betrieb', 'Passwort_Betrieb')
            else:
                print("Ungültige Auswahl")
        elif auswahl_typ == '2':
            print(" ")
            print("Registrierung:")
            print(" ")
            auswahl_art = input("Möchten Sie sich als Schüler(1) oder als Betrieb(2) registrieren? Auswahl: ")
            if auswahl_art == '1':
                register_schueler(conn)
            elif auswahl_art == '2':
                register_betrieb(conn)
            else:
                print(" ")
                print("Ungültige Auswahl")
        elif auswahl_typ == '3':
            print(" ")
            print("Abbruch")
            return
        elif auswahl_typ =="hwk-admin":
            print(" ")
            print("HWK-Admin Anmeldung:")
            login(conn, 'HWK_kronenburg', 'Benutzername', 'Passwort')
        else:
            print(" ")
            print("Ungültige Auswahl")

        conn.close()
    else:
        print("Fehler! Keine Verbindung zur Datenbank.")

if __name__ == '__main__':
    main()
