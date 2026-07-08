"""
LÖSUNG 06: Log-Analyse-Tool mit argparse (Alternative zu getopt)

Beispielaufruf:  python3 Loesungen/06_argparse_log.py -i log.txt -o ergebnis.txt -b level
"""

import argparse


def zaehle(dateiname, befehl):
    zaehler = {}
    with open(dateiname, "r", encoding="utf-8") as datei:
        for zeile in datei:
            teile = zeile.strip().split(";")
            if len(teile) != 4:
                continue
            _zeit, level, user, action = teile
            if befehl == "level":
                schluessel = level
            elif befehl == "user":
                schluessel = user
            else:
                schluessel = action
            zaehler[schluessel] = zaehler.get(schluessel, 0) + 1
    return zaehler


def schreibe_ergebnis(dateiname, befehl, zaehler):
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        for schluessel, anzahl in zaehler.items():
            datei.write(f"{schluessel}: {anzahl}\n")


def main():
    parser = argparse.ArgumentParser(description="Analyse-Tool fuer Logdateien.")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--befehl", "-b", required=True,
                        choices=["level", "user", "action"])
    args = parser.parse_args()

    ergebnis = zaehle(args.input, args.befehl)
    schreibe_ergebnis(args.output, args.befehl, ergebnis)


if __name__ == "__main__":
    main()
