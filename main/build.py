# build-Skript um eine .exe Datei zu erstellen
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
    print("building...")
    subprocess.run([
        pyinstaller_path,
        script_path,
        "--collect-all", "backend",
        "--paths", ".",  # Add the current directory to the search path
    ])
    print("build finished")

if __name__ == "__main__":
    build_exe()
