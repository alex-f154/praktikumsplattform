# Funktion für den Login
def login(conn, table, username_column, password_column):
    username = input("Geben Sie den Benutzernamen ein: ").strip()
    password = input("Geben Sie das Passwort ein: ").strip()
    
    sql = f"SELECT * FROM {table} WHERE {username_column} = %s AND {password_column} = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    
    if result:
        print("\nLogin erfolgreich")
        return True  # Rückgabe eines Werts zur Bestätigung des erfolgreichen Logins
    else:
        print("\nBenutzername oder Passwort falsch!\n")
        return False