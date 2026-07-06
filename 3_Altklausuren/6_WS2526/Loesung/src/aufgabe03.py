"""
Aufgabe 3 - Klausur Programmierung WS2025/26

Kleines Analyse-Tool fuer Logdateien im Format:
YYYY-MM-DD HH:MM:SS;LEVEL;USER;ACTION

Beispielaufruf:
    python3 aufgabe03.py -i log.txt -o ergebnis.txt -b level
"""

import sys
import getopt
from collections import Counter


def parse_zeile(zeile):
    """
    Zerlegt eine Logzeile im Format "YYYY-MM-DD HH:MM:SS;LEVEL;USER;ACTION"
    in ihre Bestandteile. Gibt None zurueck, wenn die Zeile nicht dem
    erwarteten Format entspricht (z.B. leere Zeile).
    """
    teile = zeile.strip().split(";")
    if len(teile) != 4:
        return None
    _zeitstempel, level, user, action = teile
    return level, user, action


def werte_logdatei_aus(pfad, befehl):
    """
    Liest die Logdatei unter `pfad` ein und zaehlt je nach `befehl` die
    Vorkommen pro ACTION, USER oder LEVEL. Gibt ein Counter-Objekt zurueck.
    """
    zaehler = Counter()
    with open(pfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            geparst = parse_zeile(zeile)
            if geparst is None:
                continue
            level, user, action = geparst
            if befehl == "actions":
                zaehler[action] += 1
            elif befehl == "user":
                zaehler[user] += 1
            elif befehl == "level":
                zaehler[level] += 1
    return zaehler


def schreibe_ergebnis(pfad, befehl, zaehler):
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        for schluessel, anzahl in zaehler.items():
            datei.write(f"{schluessel}: {anzahl}\n")


def main(argv):
    inputfile = ""
    outputfile = ""
    befehl = ""

    aufruf = "aufgabe03.py -i <inputfile> -o <outputfile> -b <actions|user|level>"

    # Argumente mit getopt einlesen:
    #   kurze Flags mit ':' erwarten ein Argument (i:o:b:), -h ohne Argument.
    try:
        opts, args = getopt.getopt(
            argv, "i:o:b:h",
            ["input=", "output=", "befehl=", "help"]
        )
    except getopt.GetoptError:
        print(aufruf)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(aufruf)
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt in ("-b", "--befehl"):
            befehl = arg

    # Pflichtargumente pruefen (getopt kennt kein 'required')
    if inputfile == "" or outputfile == "" or befehl == "":
        print("Fehler: -i, -o und -b sind erforderlich.")
        print(aufruf)
        sys.exit(2)

    # gueltige Befehle pruefen (getopt kennt kein 'choices')
    if befehl not in ("actions", "user", "level"):
        print("Fehler: -b muss 'actions', 'user' oder 'level' sein.")
        sys.exit(2)

    zaehler = werte_logdatei_aus(inputfile, befehl)
    schreibe_ergebnis(outputfile, befehl, zaehler)


if __name__ == "__main__":
    main(sys.argv[1:])
