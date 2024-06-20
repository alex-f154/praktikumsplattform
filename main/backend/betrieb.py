import os
import datetime

# funktion zur registrierung von praktikumsplätzen
def registrierung_praktikumsplatz(conn, betrieb_id):
    while True:
        try:
            Verfügbarkeit = input("Verfügbarkeit (YYYY-MM-DD): ").strip()
            # prüfen ob Datum im richtigen Format ist
            datetime.datetime.strptime(Verfügbarkeit, "%Y-%m-%d")
            break
        except ValueError:
            os.system('cls')
            print("\nUngültiges Datum! Bitte geben Sie das Datum im Format YYYY-MM-DD ein.\n")

    while True:
        print("Bezahlung?\n    [1] Ja\n    [2] Nein")
        Bezahlung = input("Auswahl: ").strip()
        if Bezahlung == '1':
            Bezahlung = True
            break
        elif Bezahlung == '2':
            Bezahlung = False
            break
        else:
            os.system('cls')
            print("\nUngültige Auswahl! Bitte wählen Sie [1] für Ja oder [2] für Nein.\n")

    Zeitraum = input("Zeitraum: ").strip()
    Beruf = input("Beruf: ").strip()

    sql = '''INSERT INTO Praktikumsplatz (Verfügbarkeit, Bezahlung, Zeitraum, Beruf, BetriebID) 
             VALUES (%s, %s, %s, %s, %s)'''
    cursor = conn.cursor()
    cursor.execute(sql, (Verfügbarkeit, Bezahlung, Zeitraum, Beruf, betrieb_id))
    conn.commit()
    print("Praktikumsplatz erfolgreich angeboten\n")

# funktion zum anzeigen von praktikumsplätzen
def anzeigen_praktikumsplaetze_betrieb(conn, betrieb_id):
    cursor = conn.cursor()
    sql = '''SELECT PlatzID, Verfügbarkeit, Bezahlung, Zeitraum, Beruf 
             FROM Praktikumsplatz 
             WHERE BetriebID = %s'''
    cursor.execute(sql, (betrieb_id,))
    rows = cursor.fetchall()

    if rows:
        print("\nAngebotene Praktikumsplätze:")
        for row in rows:
            print(f"Verfügbarkeit: {row[1]}, Bezahlung: {'Ja' if row[2] else 'Nein'}, Zeitraum: {row[3]}, Beruf: {row[4]}")
    else:
        print("\nKeine Praktikumsplätze gefunden.")
