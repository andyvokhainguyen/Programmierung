"""
Übung 04: Kommandozeilenargumente mit sys.argv (Skript 03)

Einfachste Form, Argumente einzulesen (ohne getopt/argparse).
Aufruf z.B.:  python3 04_sys_argv.py 3 4 5
"""

import sys


def main():
    # ✍️ SELBST:
    #   Prüfen, ob genau 3 Argumente übergeben wurden:
    #     if len(sys.argv) != 4:            # sys.argv[0] ist der Programmname!
    #         print("Aufruf: python 04_sys_argv.py <a> <b> <c>")
    #         sys.exit()
    #   a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    #   (Zahlen brauchen int(...)/float(...)!)
    #   Ergebnis ausgeben
    if len(sys.argv) != 4:
        print("Aufruf: python 04_sys_argv.py <a> <b> <c>")
        sys.exit()
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    print("Summe:", a + b+ c)


if __name__ == "__main__":
    main()
