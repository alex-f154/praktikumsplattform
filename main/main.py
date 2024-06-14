# Importieren der benutzerdefinierten Module aus dem 'backend'-Ordner
from backend.sql_connector import create_connection
from backend.registrierung import register_schueler, register_betrieb
from backend.login import login, schueler_menu, betrieb_menu, hwk_menu

# Hauptfunktion zum Ausführen des Programms
def main():
    database = "praktikumsplattform"
    conn = create_connection("localhost", "root", "", database)

    if conn is not None:
        while True:
            # Benutzerentscheidung für Login oder Registrierung | HWK-Admin Anmeldung verborgen
            print("Möchten Sie sich:")
            print("1) Anmelden")
            print("2) Registrieren")
            print("3) Abbrechen")
            auswahl_typ = input("Auswahl: ")

            if auswahl_typ == '1':
                print("\nLogin: ")
                auswahl_art = input("Sind Sie ein Schüler(1) oder ein Betrieb(2)? \nAuswahl: ")
                if auswahl_art == '1':
                    user_type = login(conn, 'Schueler', 'Username_Schueler', 'Passwort_Schueler')
                    if user_type:
                        schueler_menu()
                elif auswahl_art == '2':
                    user_type = login(conn, 'Betrieb', 'Username_Betrieb', 'Passwort_Betrieb')
                    if user_type:
                        betrieb_menu()
                else:
                    print("Ungültige Auswahl \n")
            elif auswahl_typ == '2':
                print("Registrierung: \n")
                auswahl_art = input("Möchten Sie sich als Schüler(1) oder als Betrieb(2) registrieren? \nAuswahl: ")
                if auswahl_art == '1':
                    register_schueler(conn)
                elif auswahl_art == '2':
                    register_betrieb(conn)
                else:
                    print("Ungültige Auswahl \n")
            elif auswahl_typ == '3':
                print("Abbruch \n")
                break
            elif auswahl_typ == 'hwk-admin':
                print("HWK-Admin Anmeldung: \n")
                user_type = login(conn, 'HWK_kronenburg', 'Benutzername', 'Passwort')
                if user_type:
                    hwk_menu()
            else:
                print("Ungültige Auswahl \n")

        conn.close()
    else:
        print("Fehler! Keine Verbindung zur Datenbank. \n")

if __name__ == '__main__':
    main()