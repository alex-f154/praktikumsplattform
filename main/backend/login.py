# Funktion für den Login
def login(conn, table, username_column, password_column):
    username = input("Geben Sie den Benutzernamen ein: ")
    password = input("Geben Sie das Passwort ein: ")
    
    sql = f"SELECT * FROM {table} WHERE {username_column} = %s AND {password_column} = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    
    if result:
        print("Login erfolgreich")
        # funktion die zu einem Menüpunkt führt, da muss aber zwischen schüler betrieb und hwk getrennt werden
    else:
        print("Benutzername oder Passwort falsch")