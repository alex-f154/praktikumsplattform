# Funktion zur Anzeige des Hauptmenüs
def display_main_menu():
    print("Möchten Sie sich:")
    print("  [1] Anmelden")
    print("  [2] Registrieren")
    print("  [3] Abbrechen")
    print()

# Menü für Schüler
def schueler_menu():
    while True:
        print("\nSchüler Menü:")
        print("  [1] Option 1")
        print("  [2] Option 2")
        print("  [3] Abmelden")
        auswahl = input("\nAuswahl: ").strip()
        if auswahl == '1':
            print("Option 1 gewählt")
        elif auswahl == '2':
            print("Option 2 gewählt")
        elif auswahl == '3':
            print("Abmelden")
            break
        else:
            print("Ungültige Auswahl")

# Menü für Betrieb
def betrieb_menu():
    while True:
        print("\nBetrieb Menü:")
        print("  [1] Option 1")
        print("  [2] Option 2")
        print("  [3] Abmelden")
        auswahl = input("\nAuswahl: ").strip()
        if auswahl == '1':
            print("Option 1 gewählt")
        elif auswahl == '2':
            print("Option 2 gewählt")
        elif auswahl == '3':
            print("Abmelden")
            break
        else:
            print("Ungültige Auswahl")

# Menü für HWK Kronenburg
def hwk_menu():
    while True:
        print("\nHWK Menü:")
        print("  [1] Option 1")
        print("  [2] Option 2")
        print("  [3] Abmelden")
        auswahl = input("\nAuswahl: ").strip()
        if auswahl == '1':
            print("Option 1 gewählt")
        elif auswahl == '2':
            print("Option 2 gewählt")
        elif auswahl == '3':
            print("Abmelden")
            break
        else:
            print("Ungültige Auswahl")