"""
LÖSUNG 04: Kommandozeilenargumente mit sys.argv

Aufruf z.B.:  python3 Loesungen/04_sys_argv.py 3 4 5
"""

import sys


def main():
    if len(sys.argv) != 4:                 # sys.argv[0] = Programmname
        print("Aufruf: python 04_sys_argv.py <a> <b> <c>")
        sys.exit()
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    print("Summe:", a + b + c)


if __name__ == "__main__":
    main()
