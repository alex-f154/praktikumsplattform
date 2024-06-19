import os

# Funktion für den Login
def login(conn, table, username_column, password_column):
    os.system('cls')
    print(table, "Anmeldung:\n")
    username = input("  Benutzername:   ").strip()
    password = input("  Passwort:       ").strip()
    
    sql = f"SELECT * FROM {table} WHERE {username_column} = %s AND {password_column} = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    
    if result:
        os.system('cls')
        print("Login erfolgreich")
        return result  # Rückgabe des gesamten Datensatzes
    else:
        print("\nBenutzername oder Passwort falsch!\n")
        return False