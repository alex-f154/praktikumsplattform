# Funktion für den Login
def login(conn, table, username_column, password_column):
    username = input("Geben Sie den Benutzernamen ein: ")
    password = input("Geben Sie das Passwort ein: ")
    
    sql = f"SELECT * FROM {table} WHERE {username_column} = %s AND {password_column} = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    
    if result:
        print("\nLogin erfolgreich")
        return True  # Rückgabe eines Werts zur Bestätigung des erfolgreichen Logins
    else:
        print("Benutzername oder Passwort falsch")
        return False

# Menü für Schüler
def schueler_menu():
    while True:
        print("\nSchüler Menü:")
        print("1) Option 1")
        print("2) Option 2")
        print("3) Abmelden")
        auswahl = input("Auswahl: ")
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
        print("1) Option 1")
        print("2) Option 2")
        print("3) Abmelden")
        auswahl = input("Auswahl: ")
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
        print("1) Option 1")
        print("2) Option 2")
        print("3) Abmelden")
        auswahl = input("Auswahl: ")
        if auswahl == '1':
            print("Option 1 gewählt")
        elif auswahl == '2':
            print("Option 2 gewählt")
        elif auswahl == '3':
            print("Abmelden")
            break
        else:
            print("Ungültige Auswahl")
