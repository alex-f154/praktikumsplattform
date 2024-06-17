import os

# Importieren der benutzerdefinierten Module aus dem 'backend'-Ordner
from backend.sql_connector import create_connection
from backend.registrierung import register_schueler, register_betrieb
from backend.login import login
from backend.menu import display_main_menu, schueler_menu, betrieb_menu, hwk_menu

# Hauptfunktion des Programms
def main():
    database = "praktikumsplattform"
    conn = create_connection("localhost", "root", "", database)

    if conn is not None:
        while True:
            display_main_menu()
            auswahl_typ = input("Auswahl: ").strip()
            os.system('cls') # 

            if auswahl_typ == '1':
                print("\nLogin:")
                print("  [1] Schüler")
                print("  [2] Betrieb")
                auswahl_art = input("\nAuswahl: ").strip()
                if auswahl_art == '1':
                    user_type = login(conn, 'Schueler', 'Username_Schueler', 'Passwort_Schueler')
                    if user_type:
                        schueler_menu()
                elif auswahl_art == '2':
                    user_type = login(conn, 'Betrieb', 'Username_Betrieb', 'Passwort_Betrieb')
                    if user_type:
                        betrieb_menu()
                else:
                    print("\nUngültige Auswahl\n")
            elif auswahl_typ == '2':
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
                print("\nAbbruch\n")
                break
            elif auswahl_typ == 'hwk-admin':
                print("\nHWK-Admin Anmeldung:\n")
                user_type = login(conn, 'HWK_kronenburg', 'Benutzername', 'Passwort')
                if user_type:
                    hwk_menu()
            else:
                print("\nUngültige Auswahl\n")

        conn.close()
    else:
        print("\nFehler! Keine Verbindung zur Datenbank.\n")

if __name__ == '__main__':
    main()