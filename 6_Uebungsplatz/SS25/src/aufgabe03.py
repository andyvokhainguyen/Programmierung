"""
Aufgabe 3 - Klausur Programmierung
"""
import argparse

def zaehle(dateiname, befehl):
    anzahl = 0
    with open(dateiname, "r", encoding="utf-8") as datei:
        for zeile in datei:
            if zeile.strip() == "":
                continue
            if befehl == "count":
                anzahl += 1
            elif befehl == "errors":
                if "ERROR" in zeile:
                    anzahl += 1
            elif befehl == "warnings":
                if "WARNING" in zeile:
                    anzahl += 1
    return anzahl

def schreibe_ergebnis(dateiname, befehl, ergebnis):
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        datei.write(f"Ergebnis: {ergebnis}\n")

def erstelle_parser():
    parser = argparse.ArgumentParser(
        description="Analyse-Tool fuer Logdateien"
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Name der Eingabedatei"
    )
    parser.add_argument(
        "--output", "-o", required=True,
        help="Ausgabedatei"
    )
    parser.add_argument(
        "--befehl", "-b", required=True,
        choices=["count", "errors", "warnings"],
        help="Auszuführender Befehl"
    )
    return parser

def main():
    parser = erstelle_parser()
    args = parser.parse_args()

    ergebnis = zaehle(args.input, args.befehl)
    schreibe_ergebnis(args.output, args.befehl, ergebnis)

if __name__ == "__main__":
    main()