# funktion für das anzeigen der aktuell verfügbaren praktikumsplätze
def anzeigen_praktikumsplaetze_schueler(conn):
    cursor = conn.cursor()
    sql = '''SELECT PlatzID, Verfügbarkeit, Bezahlung, Zeitraum, Beruf 
             FROM Praktikumsplatz'''
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows:
        print("\nVerfügbare Praktikumsplätze:")
        for row in rows:
            print(f"Verfügbarkeit: {row[1]}, Bezahlung: {'Ja' if row[2] else 'Nein'}, Zeitraum: {row[3]}, Beruf: {row[4]}")
    else:
        print("\nKeine verfügbaren Praktikumsplätze gefunden.")
