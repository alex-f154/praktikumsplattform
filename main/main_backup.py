import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../module')))

from sql_connector import create_connection
from registrierung import register_betrieb, register_schueler
from login import login

# Hauptfunktion zum Ausführen des Programms
def main():
    database = "praktikumsplattform"
    conn = create_connection("localhost", "root", "", database)

    if conn is not None:

        # Benutzerentscheidung für Login oder Registrierung
        print("Möchten Sie sich: ")
        print("Anmelden     (1)" )
        print("Registrieren (2) ")
        print("Abbrechen    (3) ")
        auswahl_typ = input("Bitte wählen Sie (1), (2) oder (3): ")

        if auswahl_typ == '1':
            print("Login:")
            auswahl_art = input("Sind Sie ein Schüler(1) oder ein Betrieb(2)? ")
            if auswahl_art == '1':
                login(conn, 'Schueler', 'Username_Schueler', 'Passwort_Schueler')
            elif auswahl_art == '2':
                login(conn, 'betriebe', 'Username_Betrieb', 'Passwort_Betrieb')
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
        elif auswahl_typ =="HWK-login":
            print("ADMIN ANMELDUNG######s")
            login(conn, 'HWK_kronenburg', 'Benutzername', 'Passwort')
        else:
            print("Ungültige Auswahl")

        conn.close()
    else:
        print("Fehler! Keine Verbindung zur Datenbank.")

if __name__ == '__main__':
    main()
