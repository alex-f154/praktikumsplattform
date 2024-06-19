import os
from backend.betrieb import registrierung_praktikumsplatz, anzeigen_praktikumsplaetze

# Funktion zur Anzeige des Hauptmenüs
def display_main_menu():
    os.system('cls')
    print("Möchten Sie sich:")
    print("  [1] Anmelden")
    print("  [2] Registrieren")
    print("  [3] Beenden")
    print()

# Menü für Schüler
def schueler_menu(conn):
    while True:
        print("\nSchüler Menü:")
        print("  [1] Praktikumsplätze einsehen")
        print("  [2] Option 2")
        print("  [3] Abmelden")
        auswahl = input("\nAuswahl: ").strip()
        if auswahl == '1':
            print("\nPraktikumsplätze: ")
        elif auswahl == '2':
            print("\nOption 2")
        elif auswahl == '3':
            print("Abmelden")
            break
        else:
            print("Ungültige Auswahl")

# Menü für Betrieb
def betrieb_menu(conn, betrieb_id):
    while True:
        print("\nBetrieb Menü:")
        print("  [1] Praktikumsplatz anbieten")
        print("  [2] Aktuelle Praktikas ansehen")
        print("  [3] Abmelden")
        auswahl = input("\nAuswahl: ").strip()
        if auswahl == '1':
            os.system('cls')
            print("Praktikumsplatz anbieten: \n")
            registrierung_praktikumsplatz(conn, betrieb_id) # funktion der registrierung von praktikumsplätzen
        elif auswahl == '2':
            os.system('cls')
            print("Aktuelle Praktikas: ")
            anzeigen_praktikumsplaetze(conn, betrieb_id) # funktion des anzeigen der praktikumsplätze, die man selbst anbietet
        elif auswahl == '3':
            print("Abmelden")
            break
        else:
            print("Ungültige Auswahl")

# Menü für HWK Kronenburg
def hwk_menu(conn):
    while True:
        print("\nHWK Menü:")
        print("  [1] Schüler ansehen")
        print("  [2] Betriebe ansehen")
        print("  [3] Praktikumsangebote ansehen")
        print("  [4] Praktikumsvereinbarungen ansehen **IN PROGRESS**")
        print("  [5] Abmelden")
        auswahl = input("\nAuswahl: ").strip()
        if auswahl == '1':
            os.system('cls')
            print("\nSchüler: ")
            # funktion schüler aufrufen
            cursor = conn.cursor()
            cursor.execute("SELECT username_schueler AS 'Name', Ort, Wunschberuf FROM Schueler")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        elif auswahl == '2':
            os.system('cls')
            print("\nBetriebe: ")
            # FUNKTION BETRIEBE ANSEHEN
            cursor = conn.cursor()
            cursor.execute("SELECT username_betrieb AS 'Name', Ort, Strasse FROM betrieb")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            
        elif auswahl == '3':
            print("\nPraktikumsangebote: ")
            # FUNKTION PRAKTIKUMSANGEBOTE
        elif auswahl == '4':
            print("\nPraktikumsvereinbarungen: ")
            # FUNKTION PRAKTIKUMSVEREINBARUNG
        elif auswahl == '5':
            print("Abmelden\n")
            break
        else:
            print("Ungültige Auswahl")