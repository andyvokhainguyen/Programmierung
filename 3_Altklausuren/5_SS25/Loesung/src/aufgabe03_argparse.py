"""
Aufgabe 3 - Klausur Programmierung (ALTERNATIVE mit argparse)

Gleiche Funktion wie aufgabe03.py, aber die Kommandozeile wird mit
argparse statt getopt eingelesen. Die Datei log.txt wird direkt gelesen.

Hinweis: In der Klausur ist laut Hilfsmittelblatt nur getopt erlaubt -
diese Variante dient nur zum Vergleich.

Beispielaufruf:
    python3 aufgabe03_argparse.py -o ergebnis.txt -b errors
"""

import argparse


def zaehle(befehl):
    """
    Liest die Datei log.txt zeilenweise ein und wertet sie je nach
    `befehl` aus:
    - count    : Anzahl aller (nicht leeren) Zeilen
    - errors   : Anzahl der Zeilen, die das Wort ERROR enthalten
    - warnings : Anzahl der Zeilen, die das Wort WARNING enthalten
    """
    anzahl = 0
    with open("log.txt", "r", encoding="utf-8") as datei:
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


def schreibe_ergebnis(pfad, befehl, ergebnis):
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        datei.write(f"Ergebnis: {ergebnis}\n")


def erstelle_parser():
    parser = argparse.ArgumentParser(
        description="Analyse-Tool, das die Datei log.txt einliest."
    )
    parser.add_argument(
        "--output", "-o", required=False,
        help="Name der Ausgabedatei (optional; ohne -o wird direkt ausgegeben)"
    )
    parser.add_argument(
        "--befehl", "-b", required=True,
        choices=["count", "errors", "warnings"],
        help="Auszufuehrender Befehl: 'count', 'errors' oder 'warnings'"
    )
    return parser


def main():
    parser = erstelle_parser()
    args = parser.parse_args()

    ergebnis = zaehle(args.befehl)

    if args.output:
        schreibe_ergebnis(args.output, args.befehl, ergebnis)
    else:
        print(f"Befehl: {args.befehl}")
        print(f"Ergebnis: {ergebnis}")


if __name__ == "__main__":
    main()
