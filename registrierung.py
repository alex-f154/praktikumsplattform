# Funktion zur Registrierung eines neuen Schülers
def register_schueler(conn):
    zustimmung = input("Stimmen Sie der Speicherung personenbezogener Daten zu? Ja(1), Nein(2) ")

    if zustimmung == "1":
        print("Speicherung Personenbezogener Daten zugestimmt.")
        username = input("Geben Sie den Benutzernamen ein: ")
        # Passwort-Eingabe und Bestätigung
        while True:
            password = input("Geben Sie das Passwort ein: ")
            password_confirm = input("Geben Sie das Passwort erneut ein: ")
            if password == password_confirm:
                # Passwort darf max. 16 Zeichen enthalten
                if len(password) <= 16:
                    break
                else:
                    print("Das Passwort darf nicht länger als 16 Zeichen sein.")
            else:
                print("Passwörter stimmen nicht überein. Bitte erneut eingeben.")
        wunschberuf = input("Geben Sie den Wunschberuf ein: ")
        strasse = input("Geben Sie die Straße ein: ")
        ort = input("Geben Sie den Ort ein: ")

        sql = '''INSERT INTO Schueler (Username_Schueler, Passwort_Schueler, Wunschberuf, Strasse, Ort) 
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
                # Passwort darf max. 16 Zeichen enthalten
                if len(password) <= 16:
                    break
                else:
                    print("Das Passwort darf nicht länger als 16 Zeichen sein.")
            else:
                print("Passwörter stimmen nicht überein. Bitte erneut eingeben.")
    strasse = input("Geben Sie die Straße ein: ")
    ort = input("Geben Sie den Ort ein: ")

    sql = '''INSERT INTO Betrieb (Username_Betrieb, Passwort_Betrieb, Strasse, Ort)
             VALUES (%s, %s, %s, %s)'''
    cursor = conn.cursor()
    cursor.execute(sql, (username, password, strasse, ort))
    conn.commit()
    print("Betrieb erfolgreich registriert")