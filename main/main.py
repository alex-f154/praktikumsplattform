import os

import os

# Importieren der benutzerdefinierten Module aus dem 'backend'-Ordner
from backend.sql_connector import create_connection
from backend.registrierung import register_schueler, register_betrieb
from backend.login import login
from backend.menu import display_main_menu, schueler_menu, betrieb_menu, hwk_menu

# Hauptfunktion des Programms
def main():
    database = "praktikumsplattform"
    conn = create_connection("localhost", "root", "", database) # conn repräsentiert die verbindung zur datenbank, wird benutzt um abfragen auszuführen und transaktionen zu steuern

    if conn is not None:
        while True:
            display_main_menu()
            auswahl_typ = input("Auswahl: ").strip()
            os.system('cls')

            if auswahl_typ == '1':
                os.system('cls')
                print("Login:")
                print("  [1] Schüler")
                print("  [2] Betrieb")
                auswahl_art = input("\nAuswahl: ").strip()
                if auswahl_art == '1':
                    user_type = login(conn, 'Schueler', 'Username_Schueler', 'Passwort_Schueler')
                    if user_type:
                        schueler_menu(conn)
                elif auswahl_art == '2':
                    user = login(conn, 'Betrieb', 'Username_Betrieb', 'Passwort_Betrieb')
                    if user:
                        betrieb_id = user[0]  # Annahme: BetriebID ist die erste Spalte im Ergebnis
                        betrieb_menu(conn, betrieb_id)
                else:
                    print("\nUngültige Auswahl\n")
            elif auswahl_typ == '2':
                os.system('cls')
                print("\nRegistrierung:")
                print("  [1] Schüler")
                print("  [2] Betrieb")
                auswahl_art = input("\nAuswahl: ").strip()
                if auswahl_art == '1':
                    register_schueler(conn)
                elif auswahl_art == '2':
                    register_betrieb(conn)
                else:
                    print("\nUngültige Auswahl\n")
            elif auswahl_typ == '3':
                os.system('cls')
                print("\nProgramm Beenden\n")
                break
            elif auswahl_typ == 'hwk-admin':
                print("\nHWK-Admin Anmeldung:\n")
                user_type = login(conn, 'HWK_kronenburg', 'Benutzername', 'Passwort')
                if user_type:
                    hwk_menu(conn)
            else:
                print("\nUngültige Auswahl\n")

        conn.close()
    else:
        print("\nFehler! Keine Verbindung zur Datenbank.\n")

if __name__ == '__main__':
    main()