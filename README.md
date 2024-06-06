# README

## Projektübersicht

### Zielsetzung
Unser Ziel ist die Entwicklung einer Anwendung in Python, die eine SQL-Datenbank zur Verwaltung und Vermittlung von Praktikumsplätzen verwendet. Die Anwendung soll verschiedene Funktionalitäten für Schüler und Betriebe bereitstellen, die in drei Zugriffsarten kategorisiert werden.

### Funktionen

1. **Benutzeranmeldung und -erstellung:**
   - Nutzer können sich anmelden und ein Benutzerkonto erstellen.
   - Bei der Anmeldung müssen Nutzer der Speicherung personenbezogener Daten zustimmen. Andernfalls ist keine Registrierung möglich.

2. **Verfügbare Praktikumsplätze einsehen:**
   - Schüler können verfügbare Praktikumsplätze nach Beruf, Betrieb, Zeitraum und Bezahlung (ja/nein) einsehen.

3. **Wunschberuf:**
   - Nutzer können einen Wunschberuf angeben und eine Abfrage starten, welche Betriebe Praktika in diesem Beruf anbieten.

4. **Getroffene Vereinbarungen einsehen:**
   - Nutzer können ihre getroffenen Vereinbarungen einsehen. Dies erfolgt durch eine einfache Abfrage.

5. **Berufsnachfrage analysieren:**
   - Die Anwendung bietet eine Analyse der Nachfrage nach bestimmten Berufen durch Abfragen der Anzahl der Wunschberufe.

6. **Werbemaßnahmen als Empfehlung:**
   - Bei Erfüllung bestimmter Voraussetzungen werden Empfehlungen für Werbemaßnahmen ausgegeben.

7. **Praktikumsplätze anbieten:**
   - Betriebe können Praktikumsplätze anbieten. Dies erfolgt durch das Eintragen der relevanten Informationen.

8. **Benachrichtigungen:**
   - Schüler werden benachrichtigt, wenn ein Praktikumsplatz für ihren Wunschberuf frei wird.
   - Betriebe werden benachrichtigt, wenn eine Bewerbung für einen ihrer Praktikumsplätze eingeht.

9. **Bewerbung auf Praktikumsplätze:**
   - Schüler sehen eine Liste mit verfügbaren Praktikumsplätzen inklusive einer ID.
   - Schüler können sich bewerben, indem sie die ID des gewünschten Platzes eingeben und ihre Bewerbung bestätigen (ja/nein).
   - Betriebe sehen nur Bewerbungen mit dem Status „ja“. Bewerbungen mit „nein“ oder „leer“ werden ausgeblendet.

## Zugriffsarten

1. **Schüler:**
   - Können verfügbare Praktikumsplätze einsehen.
   - Können nach Wunschberufen suchen und sich auf Praktikumsplätze bewerben.
   - Erhalten Benachrichtigungen über verfügbare Plätze in ihrem Wunschberuf.
   - Können getroffene Vereinbarungen einsehen.

2. **Betriebe:**
   - Können Praktikumsplätze anbieten.
   - Erhalten Benachrichtigungen bei eingegangenen Bewerbungen.
   - Können Bewerbungen einsehen, die den Status „ja“ haben.

3. **Administratoren:**
   - Verwalten die Datenbank und Benutzerkonten.
   - Überwachen die Analyse der Berufsnachfrage.
   - Setzen Empfehlungen für Werbemaßnahmen um.

## Installation und Einrichtung

### Voraussetzungen

- Python 3.x
- Eine SQL-Datenbank (z.B. MySQL, PostgreSQL)
- Abhängigkeiten, die in `requirements.txt` aufgeführt sind

### Installation

1. **Python und Abhängigkeiten installieren:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Datenbank einrichten:**

   - Erstellen Sie eine neue SQL-Datenbank.
   - Führen Sie die SQL-Skripte aus dem Ordner `db` aus, um die erforderlichen Tabellen zu erstellen.

3. **Konfiguration:**

   - Passen Sie die Datenbankeinstellungen in der Datei `config.py` an.

### Starten der Anwendung

```bash
python main.py
```

## Nutzung

### Anmelden und Benutzer erstellen

- Starten Sie die Anwendung und folgen Sie den Anweisungen zur Anmeldung oder Registrierung.
- Stimmen Sie der Speicherung personenbezogener Daten zu, um fortzufahren.

### Verfügbare Praktikumsplätze einsehen

- Navigieren Sie zur Seite „Praktikumsplätze“.
- Filtern Sie nach Beruf, Betrieb, Zeitraum und Bezahlung.

### Wunschberuf hinzufügen und Abfragen

- Geben Sie Ihren Wunschberuf auf der entsprechenden Seite ein.
- Sehen Sie nach, welche Betriebe Praktika in diesem Beruf anbieten.

### Vereinbarungen einsehen

- Gehen Sie zur Seite „Vereinbarungen“ und sehen Sie Ihre getroffenen Vereinbarungen ein.

### Berufsnachfrage analysieren

- Nutzen Sie die Analyse-Tools, um die Nachfrage nach verschiedenen Berufen zu sehen.

### Werbemaßnahmen erhalten

- Empfehlungen werden auf der Startseite angezeigt, wenn bestimmte Voraussetzungen erfüllt sind.

### Praktikumsplätze anbieten

- Betriebe können auf der Seite „Praktikumsplätze anbieten“ neue Plätze eintragen.

### Benachrichtigungen

- Benachrichtigungen werden im Benutzerkonto angezeigt und per E-Mail verschickt.

### Bewerbung auf Praktikumsplätze

- Schüler sehen verfügbare Plätze und können sich mit der entsprechenden ID bewerben.
- Betriebe sehen Bewerbungen mit dem Status „ja“.
