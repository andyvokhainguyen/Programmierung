"""
LÖSUNG 03: Datei lesen & schreiben
"""


def lies_datei_zeilenweise(dateiname):
    with open(dateiname, "r", encoding="utf-8") as f:
        for zeile in f:
            if zeile.strip() == "":
                continue
            print(zeile.strip())


def schreibe_datei(dateiname):
    with open(dateiname, "w", encoding="utf-8") as f:
        f.write("Apfel\n")
        f.write("Banane\n")
        f.write("Kirsche\n")



schreibe_datei("demo.txt")
lies_datei_zeilenweise("demo.txt")     # Apfel / Banane / Kirsche
