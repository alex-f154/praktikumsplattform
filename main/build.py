import shutil
import subprocess
import sys

def build_exe():
    # Pfad zum main.py-Skript
    script_path = "main.py"

    # "pyinstaller.exe"-Pfad in aktueller Umgebung finden
    pyinstaller_path = shutil.which("pyinstaller")
    if pyinstaller_path is None:
        print("PyInstaller ist nicht installiert oder wurde nicht im Pfad gefunden.")
        sys.exit(1)

    # Ausführbare Datei erstellen
    print("\n******************\nbuilding...\n******************\n")
    result = subprocess.run([
        pyinstaller_path,
        script_path,
        "--collect-all",
        "backend",
        "--onefile",        # Eine einzelne ausführbare Datei erstellen
        "--console",        # Terminal-Fenster öffnen lassen
        "--paths", "."      # Add the current directory to the search path
    ])

    if result.returncode == 0:
        print("\n******************\nbuild finished\n******************\n")
    else:
        print("build failed")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()
