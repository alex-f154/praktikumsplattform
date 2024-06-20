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
            display_main_menu() # funktion von menu.py aufrufen
            auswahl_typ = input("Auswahl: ").strip() # .strip() sorgt dafür, dass überflüssige leerzeichen bei der eingabe entfernt werden
            os.system('cls') # im terminal ein cls befehl ausführen, damit alles was davor im terminal stand, gelöscht wird für übersichtlichkeit 
            
            if auswahl_typ == '1':
                os.system('cls')
                print("Login:")
                print("  [1] Schüler")
                print("  [2] Betrieb")
                print("  [3] Hauptmenü")
                auswahl_art = input("\nAuswahl: ").strip() # auswahl zwischen schülere oder betrieb
                if auswahl_art == '1':
                    user_type = login(conn, 'Schueler', 'Username_Schueler', 'Passwort_Schueler')
                    if user_type:
                        schueler_menu(conn) # funktion schueler_menu wird aufgerufen mit conn als übergabe
                elif auswahl_art == '2':
                    user = login(conn, 'Betrieb', 'Username_Betrieb', 'Passwort_Betrieb')
                    if user:
                        betrieb_id = user[0]  # Annahme: BetriebID ist die erste Spalte im Ergebnis in der Tabelle Betrieb
                        betrieb_menu(conn, betrieb_id) # funktion betrieb_menu wird aufgerufen mit conn und betriebs_id als übergabe 
                else:
                    print("\nHauptmenü\n")
            elif auswahl_typ == '2':
                os.system('cls')
                print("Registrierung:")
                print("  [1] Schüler")
                print("  [2] Betrieb")
                print("  [3] Hauptmenü")
                auswahl_art = input("\nAuswahl: ").strip()
                if auswahl_art == '1':
                    register_schueler(conn) # funktion register_schueler wird aufgerufen mit conn als übergabe
                elif auswahl_art == '2':
                    register_betrieb(conn) # funktion register_betrieb wird aufgerufen mit conn als übergabe
                else:
                    print("\nHauptmenü\n")
            elif auswahl_typ == '3':
                os.system('cls')
                print("\nProgramm Beenden\n")
                break
            elif auswahl_typ == 'hwk-admin':
                print("\nHWK-Admin Anmeldung:\n")
                user_type = login(conn, 'HWK_kronenburg', 'Benutzername', 'Passwort')
                if user_type:
                    hwk_menu(conn) # funktion hwk_menu wird aufgerufen mit conn als übergabe
            else:
                print("\nUngültige Auswahl\n")

        conn.close()
    else:
        print("\nFehler! Keine Verbindung zur Datenbank.\n")

if __name__ == '__main__':
    main()