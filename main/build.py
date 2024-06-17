import shutil
import subprocess
import sys
import os

def build_exe():
    # Pfad zum main.py Skript
    script_path = "main.py"

    # Pfad für den pyinstaller.exe finden
    pyinstaller_path = shutil.which("pyinstaller")
    if pyinstaller_path is None:
        print("PyInstaller ist nicht installiert oder wurde nicht gefunden!\n")
        sys.exit(1)

    # Setze Output-Pfad zu jetzigem Pfad, sodass die .exe im geradigen Pfad erstellt wird | os.getcwd erhält den Wert des gerade ausgewählten Pfades
    output_pfad = os.getcwd()

    # name für die .exe datei setzen
    exe_name = "Praktikumsplattform"

    # pfad für die symbol-datei des programms
    symbol_pfad = "logo.ico"

    # .exe-Datei bauen
    print("\n******************\nbuilding...\n******************\n") # bestätigung das es startet
    result = subprocess.run([
        pyinstaller_path,
        script_path,
        "--onefile",        # eine einzige datei erstellen
        "--console",        # terminal fenster offen lassen
        "--paths", ".",     # jetzigen pfad zur suche hinzufügen
        "--distpath", output_pfad,  # setze output pfad zu geradigem pfad
        "--specpath", output_pfad,  # setze die .spec-datei zu jetzigem pfad
        "--name", exe_name, # setze den namen der exe
        "--icon", symbol_pfad, # setze das symbol der exe
        "--noconfirm",      # bestätigung (y/n) überspringen
        "--clean",          # pyinstaller cache und temporäre dateien löschen
    ])

    if result.returncode == 0:
        print("\n******************\nbuild finished\n******************\n") # bestätigung das es fertig gebaut hat
    else:
        print("Build failed") # build fehlgeschlagen
        sys.exit(1)

if __name__ == "__main__":
    build_exe()
